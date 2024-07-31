from flask import json
from api.services.llm.logic.index import LlmIndex
from api.services.llm.logic.summary import LlmSummary

from tests import app
from tests.database import CYCLE_0, CYCLE_1, KEY_RESULT_0, KEY_RESULT_1, KEY_RESULT_CHECK_MARK_0, OBJECTIVE_0, OBJECTIVE_1, USER_0, USER_1
from tests.mocks.mock_openai import MockOpenAI


def test_index():
    '''
    Given: any okr
    When: I create the index with a key result id
    Then: I should get the same id on the object
    '''
    opt = LlmIndex(KEY_RESULT_1.id)
    assert opt.okr_id == KEY_RESULT_1.id


def test_summary_ok(app):
    '''
    Given: a minimal okr definition
    When: I ask for a summary
    Then: I should get the content dictionary with the okr formatted with empty lists
    '''
    with app.app_context():
        opt = LlmSummary(MockOpenAI(), KEY_RESULT_1.id)
        summary = json.loads(opt.summary)
        assert len(summary) == 2

        system = summary[0]
        assert system['role'] == 'system'
        assert system['content'] == opt.MESSAGE_BEHAVIOUR + \
            opt.MESSAGE_MISSION + opt.MESSAGE_MAPPING

        user = summary[1]
        assert user['role'] == 'user'
        assert user['content'] == opt.MESSAGE_USER.format({
            'key-result-title': KEY_RESULT_1.title,
            'key-result-description': KEY_RESULT_1.description,
            'key-result-objective-title': OBJECTIVE_1.title,
            'key-result-owner': f'{USER_1.first_name} {USER_1.last_name}',
            'key-result-goal': KEY_RESULT_1.goal,
            'key-result-deadline': CYCLE_1.date_end,
            'key-result-progress': [],
            'key-result-tasks': [],
            'key-result-comments': []
        })


def test_summary_ok_full(app):
    '''
    Given: a complete okr definition
    When: I ask for a summary
    Then: I should get the content dictionary with the okr formatted with lists
    '''
    with app.app_context():
        opt = LlmSummary(MockOpenAI(), KEY_RESULT_0.id)
        summary = json.loads(opt.summary)
        assert len(summary) == 2

        system = summary[0]
        assert system['role'] == 'system'
        assert system['content'] == opt.MESSAGE_BEHAVIOUR + \
            opt.MESSAGE_MISSION + opt.MESSAGE_MAPPING

        user = summary[1]
        assert user['role'] == 'user'
        assert user['content'] == opt.MESSAGE_USER.format({
            'key-result-title': KEY_RESULT_0.title,
            'key-result-description': KEY_RESULT_0.description,
            'key-result-objective-title': OBJECTIVE_0.title,
            'key-result-owner': f'{USER_0.first_name} {USER_0.last_name}',
            'key-result-goal': KEY_RESULT_0.goal,
            'key-result-deadline': CYCLE_0.date_end,
            'key-result-progress': [],
            'key-result-tasks': [f'Tarefa pendente. Responsável: {USER_0.first_name} {USER_0.last_name}. Descrição: {KEY_RESULT_CHECK_MARK_0.description}.'],
            'key-result-comments': []
        })
