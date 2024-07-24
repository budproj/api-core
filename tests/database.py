from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Engine

from api.models.db.base import Base
from api.models.db.cycle import Cycle
from api.models.db.key_result_check_mark import KeyResultCheckMark
from api.models.db.team import Team
from api.models.db.types.cycle_cadence_enum import CycleCadenceEnum
from api.models.db.user import User
from api.models.db.key_result import KeyResult
from api.models.db.objective import Objective

USER_0 = User(id='e1611b49-e1b3-4504-9457-32d66d45db17',
              first_name='David',
              last_name='Wallace')
USER_1 = User(id='41ce3848-c5b1-49f8-ad47-d82211b55de3',
              first_name='Michael',
              last_name='Scott')
USER_2 = User(id='75eb09a6-0b02-4499-bdb2-c122f79cbecc',
              first_name='Dwight',
              last_name='Schrute')
USER_3 = User(id='33846108-f39e-4455-96cb-f96ae74e256f',
              first_name='Jim',
              last_name='Halpert')
TEAM_0 = Team(id='235a43f1-0ac1-40ea-8b98-bc181a0be390',
              name='Dunder-Mifflin',
              owner_id=USER_0.id)
TEAM_1 = Team(id='b901d6ce-6357-456a-9f4b-e6c5b3e6f099',
              name='Scranton',
              description='Best branch of DM',
              owner_id=USER_1.id,
              parent_id=TEAM_0.id)
CYCLE_0 = Cycle(id='d936d789-10a5-45a4-9265-f5a0ac26a963',
                period='2013',
                cadence=CycleCadenceEnum.YEARLY,
                date_start=datetime(2013, 1, 1),
                date_end=datetime(2013, 12, 31),
                team_id=TEAM_0.id)
CYCLE_1 = Cycle(id='ed98f104-6903-4146-a565-2cbb14fb80ae',
                period='Q4',
                cadence=CycleCadenceEnum.QUARTERLY,
                date_start=datetime(2013, 10, 1),
                date_end=datetime(2013, 12, 31),
                team_id=TEAM_1.id,
                parent_id=CYCLE_0.id)
OBJECTIVE_0 = Objective(id='88950e8c-7dac-48bf-be2a-09b605724281',
                        title='Max out paper revenue',
                        team_id=TEAM_0.id,
                        cycle_id=CYCLE_0.id,
                        owner_id=USER_0.id)
OBJECTIVE_1 = Objective(id='769ab4a1-f699-4b92-9438-c5242d5998b6',
                        title='Be the best branch',
                        team_id=TEAM_1.id,
                        cycle_id=CYCLE_1.id,
                        owner_id=USER_1.id)
KEY_RESULT_0 = KeyResult(id='954c1b6f-0f16-4fe4-95c7-8f0abc96ae3c',
                         title='Sell double the paper',
                         goal=100.0,
                         initial_value=50.0,
                         objective_id=OBJECTIVE_0.id,
                         team_id=TEAM_0.id,
                         owner_id=USER_0.id)
KEY_RESULT_1 = KeyResult(id='a5f879ec-f4f7-4b10-9766-80e40edb9e2c',
                         title='Be #1 boss',
                         goal=1,
                         initial_value=1,
                         objective_id=OBJECTIVE_1.id,
                         team_id=TEAM_1.id,
                         owner_id=USER_1.id)
KEY_RESULT_2 = KeyResult(id='3bce8902-a4b9-45c1-9a9e-f33306d9de16',
                         title='Map the daily routine of everyone',
                         description='Jim may be a vampire',
                         goal=13,
                         initial_value=0,
                         objective_id=OBJECTIVE_1.id,
                         team_id=TEAM_1.id,
                         owner_id=USER_2.id)
KEY_RESULT_3 = KeyResult(id='3d7d5cf2-6778-4aed-b1f3-d449dafd6655',
                         title='Prank Dwight 100 times',
                         description='Everything is Jelly',
                         goal=100,
                         initial_value=0,
                         objective_id=OBJECTIVE_1.id,
                         team_id=TEAM_1.id,
                         owner_id=USER_3.id)
KEY_RESULT_CHECK_MARK_0 = KeyResultCheckMark(id='1e2f3349-f55a-478c-a1ba-6c1025ccc351',
                                             description='Fire Ryan',
                                             assigned_user_id=USER_0.id,
                                             key_result_id=KEY_RESULT_0.id)


def init(db: SQLAlchemy, engine: Engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    db.session.add(USER_0)
    db.session.add(USER_1)
    db.session.add(USER_2)
    db.session.add(USER_3)
    db.session.add(CYCLE_0)
    db.session.add(CYCLE_1)
    db.session.add(OBJECTIVE_0)
    db.session.add(OBJECTIVE_1)
    db.session.add(KEY_RESULT_0)
    db.session.add(KEY_RESULT_1)
    db.session.add(KEY_RESULT_2)
    db.session.add(KEY_RESULT_3)
    db.session.add(KEY_RESULT_CHECK_MARK_0)
    db.session.commit()
