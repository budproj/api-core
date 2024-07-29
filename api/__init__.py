import logging
from flask.logging import default_handler
from logging.config import dictConfig
from flask import Flask
from importlib import import_module
from flask_sqlalchemy import SQLAlchemy
from flask_openai import OpenAI

core_db = SQLAlchemy()
core_openai = OpenAI()

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


def create_app():
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
    logging.getLogger('sqlalchemy.dialects').setLevel(logging.INFO)
    logging.getLogger('sqlalchemy.pool').setLevel(logging.INFO)
    logging.getLogger('sqlalchemy.orm').setLevel(logging.INFO)

    app = Flask(__name__)
    app.config.from_object(config)
    core_db.init_app(app)
    core_openai.init_app(app)
    for module_name in ('llm',):
        module = import_module(
            'api.services.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)
    return app
