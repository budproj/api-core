import uuid
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

from .types.objective_mode_enum import ObjectiveModeEnum

from .base import Base

from .cycle import Cycle


class Objective(Base):
    __tablename__ = 'objective'
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, nullable=False)
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str]
    mode: Mapped[ObjectiveModeEnum] = mapped_column(
        nullable=False, default=ObjectiveModeEnum.PUBLISHED)

    team_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey('team.id'), nullable=False)
    cycle_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('cycle.id'))
    owner_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('user.id'))

    key_results = relationship('KeyResult', back_populates='objective')
    cycle = relationship('Cycle', back_populates='objectives')
