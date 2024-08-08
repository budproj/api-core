from api.services.llm.logic.index import LlmIndex
from api.services.llm.logic.summary import LlmSummary
from api.utils.auth import requires_auth
from api.utils.openai import OpenAI
from . import blueprint
from flask import render_template


@blueprint.route('/<key_result_id>')
@requires_auth('key-result:create')
def index(key_result_id: str):
    return render_template('index.html', opts=LlmIndex(key_result_id))


@blueprint.route('/summary/<key_result_id>')
@requires_auth('key-result:create')
def summary(key_result_id: str):
    return render_template('summary.html', opts=LlmSummary(OpenAI(), key_result_id))
