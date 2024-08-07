from flask import render_template, request
from . import blueprint
from api.services.llm.logic.index import LlmIndex
from api.services.llm.logic.summary import LlmSummary
from api.services.llm.logic.team_ranking import TeamRanking
from api.utils.openai import OpenAI


@blueprint.route('/<okr_id>')
def index(okr_id: str):
    return render_template('index.html', opts=LlmIndex(okr_id))


@blueprint.route('/summary/<okr_id>')
def summary(okr_id: str):
    return render_template('summary.html', opts=LlmSummary(OpenAI(), okr_id))


@blueprint.route('/team-ranking/<team_id>')
def team_ranking(team_id):
    cycle_id = request.args.get('cycle_id')
    return render_template('team-ranking.html', opts=TeamRanking(team_id, cycle_id))


@blueprint.route('/team-ranking/<team_id>/children')
def team_ranking_children(team_id):
    cycle_id = request.args.get('cycle_id')
    return render_template('team-ranking-content.html', opts=TeamRanking(team_id, cycle_id, load_cycles=False))
