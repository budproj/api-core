
from typing import Optional

from flask import json
from api.utils.openai import OpenAI


class MockOpenAI(OpenAI):
    def get_completion(self, message_system: str, message_user: str) -> Optional[str]:
        return json.dumps([
            {
                'role': 'system',
                'content': message_system
            },
            {
                'role': 'user',
                'content': message_user
            },
        ])
