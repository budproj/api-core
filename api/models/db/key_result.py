from typing import TYPE_CHECKING, List, Optional
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

from api.models.db.base import Base
if TYPE_CHECKING:
    from api.models.db.user import User
    from api.models.db.objective import Objective
    from api.models.db.team import Team
    from api.models.db.key_result_check_in import KeyResultCheckIn
    from api.models.db.key_result_check_mark import KeyResultCheckMark
    from api.models.db.key_result_comment import KeyResultComment
from api.models.db.types.key_result_format_enum import KeyResultFormatEnum
from api.models.db.types.key_result_mode_enum import KeyResultModeEnum
from api.models.db.types.key_result_type_enum import KeyResultTypeEnum


class KeyResult(Base):
    __tablename__ = 'key_result'
    id: Mapped[str] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[Optional[str]]
    goal: Mapped[float]
    initial_value: Mapped[float] = mapped_column()

    format: Mapped[KeyResultFormatEnum] = mapped_column(
        default=KeyResultFormatEnum.NUMBER)
    type: Mapped[KeyResultTypeEnum] = mapped_column(
        default=KeyResultTypeEnum.ASCENDING)
    mode: Mapped[KeyResultModeEnum] = mapped_column(
        default=KeyResultModeEnum.PUBLISHED)

    team_id: Mapped[str] = mapped_column(
        ForeignKey('team.id'))
    team: Mapped['Team'] = relationship(back_populates='key_results')

    objective_id: Mapped[str] = mapped_column(
        ForeignKey('objective.id'))
    objective: Mapped['Objective'] = relationship('Objective',
                                                  innerjoin=True,
                                                  back_populates='key_results')

    owner_id: Mapped[str] = mapped_column(
        ForeignKey('user.id'))
    owner: Mapped['User'] = relationship(back_populates='key_results',
                                         innerjoin=True)
    key_result_check_ins: Mapped[List['KeyResultCheckIn']] = relationship(
        back_populates='key_result')
    key_result_check_marks: Mapped[List['KeyResultCheckMark']] = relationship(
        back_populates='key_result')
    key_result_comments: Mapped[List['KeyResultComment']] = relationship(
        back_populates='key_result')
