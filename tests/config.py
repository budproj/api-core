import os
from api.config import Config


class TestConfig(Config):

    basedir = os.path.abspath(os.path.dirname(__file__))

    DB_ENGINE = 'sqlite'
    DB_HOST = f'/{basedir}'
    DB_NAME = 'test.sqlite'

    SQLALCHEMY_DATABASE_URI = \
        f'{DB_ENGINE}://{DB_HOST}/{DB_NAME}'

    OPENAI_API_KEY = 'TEST'

    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

    TESTING = True
