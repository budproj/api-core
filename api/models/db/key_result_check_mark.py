import uuid
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

from .types.key_result_format_enum import KeyResultFormatEnum
from .types.key_result_mode_enum import KeyResultModeEnum
from .types.key_result_type_enum import KeyResultTypeEnum

from .objective import Objective
from .user import User

from .base import Base


class KeyResultCheckMark(Base):
    __tablename__ = 'key_result_check_mark'
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    state: Mapped[str] = mapped_column(nullable=False)

    assigned_user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey('user.id'), nullable=False)
    key_result_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey('key_result.id'), nullable=False)

    key_result = relationship(
        'KeyResult', back_populates='key_result_check_marks')
    assigned_user = relationship(
        'User', back_populates='key_result_check_marks')
