import logging
from logging.config import dictConfig
from flask import Flask
from importlib import import_module
from flask_sqlalchemy import SQLAlchemy
from flask_openai import OpenAI

from api.config import Config

from authlib.integrations.flask_client import OAuth


core_db = SQLAlchemy()
core_openai = OpenAI()
core_oauth = OAuth()


def create_auth(config: Config):
    core_oauth.register(
        'auth0',
        client_id=config.AUTH0_CLIENT_ID,
        client_secret=config.AUTH0_CLIENT_SECRET,
        client_kwargs={
            'scope': 'openid profile email offline_access',
        },
        server_metadata_url=f'https://{
            config.AUTH0_DOMAIN}/.well-known/openid-configuration'
    )


dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'DEBUG',
        'handlers': ['wsgi']
    }
})


def create_app(config=Config()):
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
    logging.getLogger('sqlalchemy.dialects').setLevel(logging.INFO)
    logging.getLogger('sqlalchemy.pool').setLevel(logging.INFO)
    logging.getLogger('sqlalchemy.orm').setLevel(logging.INFO)

    app = Flask(__name__)
    app.config.from_object(config)
    core_db.init_app(app)
    core_openai.init_app(app)
    core_oauth.init_app(app)
    create_auth(config)

    for module_name in ('llm', 'auth'):
        module = import_module(
            'api.services.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)
    print(app.url_map)

    return app
