import uuid
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .types.objective_mode_enum import ObjectiveModeEnum

from .base import Base


class Objective(Base):
    __tablename__ = 'objective'
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, nullable=False)
    description: Mapped[str]
    mode: Mapped[ObjectiveModeEnum] = mapped_column(
        nullable=False, default=ObjectiveModeEnum.PUBLISHED)

    team_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey('team.id'), nullable=False)
    cycle_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('cycle.id'))
    owner_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('user.id'))
