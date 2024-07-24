from datetime import datetime
from typing import TYPE_CHECKING, List, Optional
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

from api.models.db.base import Base
if TYPE_CHECKING:
    from api.models.db.objective import Objective
    from api.models.db.team import Team
from api.models.db.types.cycle_cadence_enum import CycleCadenceEnum


class Cycle(Base):
    __tablename__ = 'cycle'
    id: Mapped[str] = mapped_column(primary_key=True)
    period: Mapped[str] = mapped_column()
    cadence: Mapped[CycleCadenceEnum] = mapped_column()
    active: Mapped[bool] = mapped_column(default=True)
    date_start: Mapped[datetime] = mapped_column()
    date_end: Mapped[datetime] = mapped_column()

    team_id: Mapped[str] = mapped_column(ForeignKey('team.id'))
    team: Mapped['Team'] = relationship(back_populates='cycles')

    parent_id: Mapped[Optional[str]] = mapped_column(ForeignKey('cycle.id'))
    parent: Mapped[Optional['Cycle']] = relationship(
        back_populates='children', remote_side=[id])
    children: Mapped[List['Cycle']] = relationship(back_populates='parent')

    objectives: Mapped[List['Objective']] = relationship(
        back_populates='cycle')
