from typing import Optional
from api import core_openai


class OpenAI:
    def get_completion(self, message_system: str, message_user: str) -> Optional[str]:
        completion = core_openai.client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[
                {
                    'role': 'system',
                    'content': message_system
                },
                {
                    'role': 'user',
                    'content': message_user
                },
            ]
        )
        return completion.choices[0].message.content
