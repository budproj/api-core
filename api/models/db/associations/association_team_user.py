from sqlalchemy import Column, ForeignKey, Table

from api.models.db.base import Base

association_team_user = Table(
    'team_users_user',
    Base.metadata,
    Column('user_id', ForeignKey('user.id')),
    Column('team_id', ForeignKey('team.id')),
)
