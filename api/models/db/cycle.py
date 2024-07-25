from datetime import datetime
import uuid
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

from .base import Base
from .types.cycle_cadence_enum import CycleCadenceEnum


class Cycle(Base):
    __tablename__ = 'cycle'
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, nullable=False)
    period: Mapped[str] = mapped_column(nullable=False)
    cadence: Mapped[CycleCadenceEnum] = mapped_column(nullable=False)
    active: Mapped[bool] = mapped_column(default=True, nullable=False)
    date_start: Mapped[datetime] = mapped_column(nullable=False)
    date_end: Mapped[datetime] = mapped_column(nullable=False)

    team_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey('team.id'), nullable=False)
    parent_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('cycle.id'))

    objectives = relationship('Objective', back_populates='cycle')
