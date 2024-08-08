from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from typing import TYPE_CHECKING, Optional, List

from api.models.db.associations.association_team_user import association_team_user
from api.models.db.views.team_company import association_team_company
from api.models.db.base import Base
if TYPE_CHECKING:
    from api.models.db.key_result import KeyResult
    from api.models.db.objective import Objective
    from api.models.db.user import User
    from api.models.db.cycle import Cycle


class Team(Base):
    __tablename__ = 'team'
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    description: Mapped[Optional[str]] = mapped_column()

    parent_id: Mapped[Optional[str]] = mapped_column(ForeignKey('team.id'))
    parent: Mapped[Optional['Team']] = relationship(
        back_populates='children', remote_side=[id])
    children: Mapped[List['Team']] = relationship(back_populates='parent')

    owner_id: Mapped[str] = mapped_column(
        ForeignKey('user.id'))
    owner: Mapped['User'] = relationship()

    cycles: Mapped[List['Cycle']] = relationship(back_populates='team')
    objectives: Mapped[List['Objective']] = relationship(back_populates='team')
    key_results: Mapped[List['KeyResult']
                        ] = relationship(back_populates='team')

    users: Mapped[List['User']] = relationship(
        secondary=association_team_user, back_populates='teams')

    company: Mapped['Team'] = relationship(
        secondary=association_team_company,
        primaryjoin=id == association_team_company.c.team_id,
        secondaryjoin=id == association_team_company.c.company_id,
    )
