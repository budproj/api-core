# Define the TeamCompany model representing the view
from sqlalchemy import Column, ForeignKey, Table
from api.models.db.base import Base


association_team_company = Table(
    'team_company',
    Base.metadata,
    Column('team_id', ForeignKey('team.id')),
    Column('company_id', ForeignKey('team.id')),
    Column('depth'),
)
