from flask import Flask
from importlib import import_module
from flask_sqlalchemy import SQLAlchemy
from flask_openai import OpenAI

from api.config import Config

core_db = SQLAlchemy()
core_openai = OpenAI()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    core_db.init_app(app)
    core_openai.init_app(app)
    for module_name in ('llm',):
        module = import_module('api.services.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)
    return app
