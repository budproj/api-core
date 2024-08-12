from . import blueprint
from api.services.dashboard.logic.team_ranking import TeamRanking
from flask import render_template, request


@blueprint.route('/team-ranking/<team_id>')
def team_ranking(team_id):
    cycle_id = request.args.get('cycle_id')
    return render_template('team-ranking.html', opts=TeamRanking(team_id, cycle_id))


@blueprint.route('/team-ranking/<team_id>/children')
def team_ranking_children(team_id):
    cycle_id = request.args.get('cycle_id')
    return render_template('team-ranking-content.html', opts=TeamRanking(team_id, cycle_id, load_cycles=False))
