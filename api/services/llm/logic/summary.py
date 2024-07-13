from api import core_db, core_openai
from api.models.db.key_result import KeyResult


class LlmSummary:
    summary: str

    MESSAGE_SYSTEM = 'Você é uma máquina que ajuda a pessoa a entender o conceito de objetivos e resultados-chave'
    MESSAGE_USER = 'Me ajude a entender melhor esse resultado-chave: %s'

    ERROR_SUMMARY = 'Houve um erro ao gerar o texto, tente novamente mais tarde.'

    def __init__(self, okr_id):
        okr: KeyResult = core_db.session.query(
            KeyResult).filter_by(id=okr_id).first()
        completion = core_openai.client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[
                {
                    'role': 'system',
                    'content': self.MESSAGE_SYSTEM
                },
                {
                    'role': 'user',
                    'content': self.MESSAGE_USER.format(okr.title)
                },
            ]
        )
        summary = completion.choices[0].message.content
        if summary is None:
            self.summary = self.ERROR_SUMMARY
        else:
            self.summary = summary
