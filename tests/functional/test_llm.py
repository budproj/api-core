from api.services.llm.logic.index import LlmIndex
from api.services.llm.logic.summary import LlmSummary

from tests import app
from tests.database import KEY_RESULT_0


def test_index():
    opt = LlmIndex(KEY_RESULT_0.id)
    assert opt.okr_id == KEY_RESULT_0.id


def test_summary(app):
    with app.app_context():
        opt = LlmSummary(KEY_RESULT_0.id)
        assert opt.summary is None
