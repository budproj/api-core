from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

from api.models.db.base import Base
if TYPE_CHECKING:
    from api.models.db.key_result import KeyResult
    from api.models.db.user import User


class KeyResultComment(Base):
    __tablename__ = 'key_result_comment'
    id: Mapped[str] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column()

    user_id: Mapped[str] = mapped_column(
        ForeignKey('user.id'))
    user: Mapped['User'] = relationship(
        back_populates='key_result_comments')

    key_result_id: Mapped[str] = mapped_column(
        ForeignKey('key_result.id'))
    key_result: Mapped['KeyResult'] = relationship(
        back_populates='key_result_comments')
