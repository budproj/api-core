import pytest
from sqlalchemy import create_engine
from api import create_app, core_db
from .config import Config
from .database import init


@pytest.fixture()
def app():
    config = Config()
    app = create_app(config)
    with app.app_context():
        engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
        init(core_db, engine)
        yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
