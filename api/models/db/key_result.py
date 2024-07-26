import uuid
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

from .types.key_result_format_enum import KeyResultFormatEnum
from .types.key_result_mode_enum import KeyResultModeEnum
from .types.key_result_type_enum import KeyResultTypeEnum

from .objective import Objective
from .user import User
from .key_result_check_in import KeyResultCheckIn
from .key_result_check_mark import KeyResultCheckMark
from .key_result_comment import KeyResultComment

from .base import Base


class KeyResult(Base):
    __tablename__ = 'key_result'
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, nullable=False)
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str]
    goal: Mapped[float] = mapped_column(nullable=False)
    initial_value: Mapped[float] = mapped_column(nullable=False)

    format: Mapped[KeyResultFormatEnum] = mapped_column(
        nullable=False, default=KeyResultFormatEnum.NUMBER)
    type: Mapped[KeyResultTypeEnum] = mapped_column(
        nullable=False, default=KeyResultTypeEnum.ASCENDING)
    mode: Mapped[KeyResultModeEnum] = mapped_column(
        nullable=False, default=KeyResultModeEnum.PUBLISHED)

    team_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey('team.id'))
    objective_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey('objective.id'), nullable=False)
    owner_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey('user.id'), nullable=False)

    objective = relationship('Objective',
                             innerjoin=True,
                             back_populates='key_results')
    user = relationship('User',
                        back_populates='key_results',
                        innerjoin=True)
    key_result_check_ins = relationship(
        'KeyResultCheckIn', back_populates='key_result')
    key_result_check_marks = relationship(
        'KeyResultCheckMark', back_populates='key_result')
    key_result_comments = relationship(
        'KeyResultComment', back_populates='key_result')
