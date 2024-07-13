from api.services.llm.logic.index import LlmIndex
from api.services.llm.logic.summary import LlmSummary
from . import blueprint
from flask import render_template


@blueprint.route('/<okr_id>')
def index(okr_id: str):
    return render_template('index.html', opts=LlmIndex(okr_id))


@blueprint.route('/summary/<okr_id>')
def summary(okr_id: str):
    return render_template('summary.html', opts=LlmSummary(okr_id))
