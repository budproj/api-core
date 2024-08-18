from . import blueprint
from api.services.dashboard.logic.team_ranking import TeamRanking
from flask import render_template, request


@blueprint.route('/team-ranking/<team_id>')
def team_ranking(team_id):
    cycle_ids = request.args.getlist('cycle_ids')
    return render_template('team-ranking.html', opts=TeamRanking(team_id, cycle_ids))


@blueprint.route('/team-ranking/<team_id>/children')
def team_ranking_children(team_id):
    cycle_ids = request.args.getlist('cycle_ids')
    return render_template('team-ranking-content.html', opts=TeamRanking(team_id, cycle_ids, load_cycles=False))
