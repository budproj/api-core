import pytest
from sqlalchemy import create_engine
from api import create_app, core_db
from .config import TestConfig
from .database import init


@pytest.fixture(scope='module')
def app():
    config = TestConfig()
    app = create_app(config)
    engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
    with app.app_context():
        init(core_db, engine)
        yield app
    engine.dispose()


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
