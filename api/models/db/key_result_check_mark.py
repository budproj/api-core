from typing import TYPE_CHECKING, Optional
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

from api.models.db.base import Base
from api.models.db.types.key_result_check_mark_state_enum import KeyResultCheckMarkStateEnum
if TYPE_CHECKING:
    from api.models.db.key_result import KeyResult
    from api.models.db.user import User


class KeyResultCheckMark(Base):
    __tablename__ = 'key_result_check_mark'
    id: Mapped[str] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column()
    state: Mapped[KeyResultCheckMarkStateEnum] = mapped_column(
        default=KeyResultCheckMarkStateEnum.UNCHECKED)

    assigned_user_id: Mapped[Optional[str]] = mapped_column(
        ForeignKey('user.id'))
    assigned_user: Mapped['User'] = relationship(
        back_populates='key_result_check_marks')

    key_result_id: Mapped[str] = mapped_column(
        ForeignKey('key_result.id'))
    key_result: Mapped['KeyResult'] = relationship(
        back_populates='key_result_check_marks')
