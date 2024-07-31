from typing import TYPE_CHECKING, List, Optional
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

from api.models.db.base import Base
if TYPE_CHECKING:
    from api.models.db.cycle import Cycle
    from api.models.db.key_result import KeyResult
    from api.models.db.team import Team
    from api.models.db.user import User
from api.models.db.types.objective_mode_enum import ObjectiveModeEnum


class Objective(Base):
    __tablename__ = 'objective'
    id: Mapped[str] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()
    description: Mapped[Optional[str]]
    mode: Mapped[ObjectiveModeEnum] = mapped_column(
        default=ObjectiveModeEnum.PUBLISHED)

    team_id: Mapped[str] = mapped_column(ForeignKey('team.id'))
    team: Mapped['Team'] = relationship(back_populates='objectives')

    cycle_id: Mapped[str] = mapped_column(ForeignKey('cycle.id'))
    cycle: Mapped['Cycle'] = relationship(back_populates='objectives')

    owner_id: Mapped[str] = mapped_column(ForeignKey('user.id'))
    owner: Mapped['User'] = relationship(back_populates='objectives')

    key_results: Mapped[List['KeyResult']] = relationship(
        back_populates='objective')
