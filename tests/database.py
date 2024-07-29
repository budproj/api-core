from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Engine

from api.models.db.base import Base
from api.models.db.key_result import KeyResult
from api.models.db.objective import Objective

OBJECTIVE_0 = Objective(id='88950e8c-7dac-48bf-be2a-09b605724281')
KEY_RESULT_0 = KeyResult(id='954c1b6f-0f16-4fe4-95c7-8f0abc96ae3c',
                         title='Key Result 0',
                         goal=100.0,
                         initial_value=20.0,
                         objective_id=OBJECTIVE_0.id)


def init(db: SQLAlchemy, engine: Engine):
    db.drop_all()
    Base.metadata.create_all(engine)
    db.create_all()
    db.session.add(OBJECTIVE_0)
    db.session.add(KEY_RESULT_0)
