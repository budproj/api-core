from datetime import datetime
from typing import List
from sqlalchemy import text
from api import core_db
from ast import literal_eval


class TeamRanking:
    team_id: str
    cycle_id: str
    cycles = []
    teams: List
    total_teams_progress = 0

    SQL_TEAMS_QUERY = text("""
      SELECT query.* FROM (
        SELECT
            t.name,
            t.id,
            t.parent_id,
            os.is_outdated,
            os.is_active,
            os.progress,
            os.previous_progress,
            krlci.created_at AS latest_check_in_created_at,
            u.first_name,
            u.last_name,
            u.id AS user_id,
            ROW_NUMBER() OVER(
                PARTITION BY t.name
                ORDER BY
                    CASE WHEN krlci.created_at IS NULL THEN 0 ELSE 1 END DESC,
                    krlci.created_at DESC
            ) num
        FROM team t
        INNER JOIN team_company tc ON t.id = tc.team_id
        LEFT JOIN key_result kr ON kr.team_id = tc.team_id
        LEFT JOIN key_result_latest_check_in krlci ON krlci.key_result_id = kr.id
        LEFT JOIN "user" u ON u.id = krlci.user_id
        LEFT JOIN (
            SELECT
                os.team_id,
                os.cycle_id,
                bool_and(os.is_outdated) AS is_outdated,
                bool_or(os.is_active) AS is_active,
                avg(os.progress) AS progress,
                min(os.confidence) AS confidence,
                avg(os.previous_progress) AS previous_progress,
                min(os.previous_confidence) AS previous_confidence
            FROM
                objective_status os
            GROUP BY
                os.team_id,
                os.cycle_id
        ) os ON os.team_id = tc.team_id
        WHERE t.parent_id IS NOT NULL
        AND tc.company_id = :company_id
        and os.cycle_id = :cycle_id
    ) AS query
    WHERE num = 1
    ORDER BY coalesce(progress, 0) DESC
      """)

    SQL_CYCLES_QUERY = text("""
      SELECT date_start, date_end, period, id
        FROM "cycle" c
        WHERE c.team_id = :company_id
          AND c.active = true
        """)

    def __init__(self, team_id: str, cycle_id: str = None, load_cycles=True):
        """Initializes team_id

        Args:
          team_id: team uuid to initialize on page
        """

        self.team_id = team_id
        self.cycle_id = cycle_id
        self.teams = self._get_team_ranking(team_id, cycle_id)
        self.total_teams_progress = self._calculate_total_teams_progress(
            self.teams)
        if load_cycles:
            self.cycles = self._get_cycles(team_id)

    def _get_team_ranking(self, team_id: str, cycle_id: str):

        result = core_db.session.execute(
            self.SQL_TEAMS_QUERY, {'company_id': team_id, 'cycle_id': cycle_id}).fetchall()

        formatted_result = []
        for row in result:
            formatted_result.append({
                'team_name': row[0],
                'team_id': row[1],
                'parent_id': row[2],
                'is_outdated': row[3],
                'is_active': row[4],
                'progress': row[5],
                "previous_progress": row[6],
                'latest_check_in_created_at': self._time_ago(row[7]),
                'user_first_name': row[8],
                'user_last_name': row[9],
                'user_id': row[10],
            })
        return formatted_result

    def _get_cycles(self, team_id: str):
        cycle_result = core_db.session.execute(
            self.SQL_CYCLES_QUERY, {'company_id': team_id}).fetchall()

        return [
            {
                'expected_progress': self._get_projected_progress(cycle[0], cycle[1])[1],
                'period': cycle[2],
                'id': str(cycle[3])
            }
            for cycle in cycle_result
        ]

    def _time_ago(self, past_date):
        now = datetime.now()
        diff = now - past_date

        seconds = diff.total_seconds()
        minutes = int(seconds // 60)
        hours = int(minutes // 60)
        days = int(hours // 24)

        if days > 0:
            return f"há {days} dia{'s' if days > 1 else ''}"
        elif hours > 0:
            return f"há {hours} hora{'s' if hours > 1 else ''}"
        elif minutes > 0:
            return f"há {minutes} minuto{'s' if minutes > 1 else ''}"
        else:
            return "just now"

    def _get_projected_progress(self, date_start: datetime, date_end: datetime, expected_goal: float = 0.7):
        if not date_start or not date_end:
            return 0, 0

        current_date = datetime.now()

        if current_date < date_start:
            return 0, 0
        if current_date > date_end:
            return expected_goal, expected_goal * 100

        delta_start_finish = (date_end - date_start).total_seconds()
        delta_start_current = (current_date - date_start).total_seconds()

        absolute_projected_progress = (
            delta_start_current / delta_start_finish) * expected_goal
        percentual_projected_progress = absolute_projected_progress * 100

        return absolute_projected_progress, percentual_projected_progress

    def _calculate_total_teams_progress(self, teams):
        total_progress = sum(team['progress'] for team in teams)
        num_teams = len(self.teams)
        average_progress = total_progress / num_teams if num_teams > 0 else 0
        return average_progress
