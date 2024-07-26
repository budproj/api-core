import os


class Config(object):

    basedir = os.path.abspath(os.path.dirname(__file__))

    DB_ENGINE = os.environ['DB_ENGINE']
    DB_USERNAME = os.environ['DB_USERNAME']
    DB_PASS = os.environ['DB_PASS']
    DB_HOST = os.environ['DB_HOST']
    DB_PORT = os.environ['DB_PORT']
    DB_NAME = os.environ['DB_NAME']

    SQLALCHEMY_DATABASE_URI = \
        f'{DB_ENGINE}://{DB_USERNAME}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

    OPENAI_API_KEY = os.environ['OPENAI_API_KEY']

    AUTH0_CLIENT_ID = os.environ['AUTH0_CLIENT_ID']
    AUTH0_CLIENT_SECRET = os.environ['AUTH0_CLIENT_SECRET']
    AUTH0_DOMAIN = os.environ['AUTH0_DOMAIN']
    AUTH0_AUDIENCE = os.environ['AUTH0_AUDIENCE']

    DEBUG = (os.getenv('DEBUG', 'False') == 'True')
    if not DEBUG:
        # Security
        SESSION_COOKIE_HTTPONLY = True
        REMEMBER_COOKIE_HTTPONLY = True
        REMEMBER_COOKIE_DURATION = 3600
