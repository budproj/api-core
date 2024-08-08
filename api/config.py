import os


class Config(object):

    basedir = os.path.abspath(os.path.dirname(__file__))

    DB_ENGINE = os.getenv('DB_ENGINE', '')
    DB_USERNAME = os.getenv('DB_USERNAME', '')
    DB_PASS = os.getenv('DB_PASS', '')
    DB_HOST = os.getenv('DB_HOST', '')
    DB_PORT = os.getenv('DB_PORT', '')
    DB_NAME = os.getenv('DB_NAME', '')

    SQLALCHEMY_DATABASE_URI = \
        f'{DB_ENGINE}://{DB_USERNAME}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')

    DEBUG = (os.getenv('DEBUG', 'False') == 'True')
    if not DEBUG:
        # Security
        SESSION_COOKIE_HTTPONLY = True
        REMEMBER_COOKIE_HTTPONLY = True
        REMEMBER_COOKIE_DURATION = 3600
