from typing import TYPE_CHECKING
from .base import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

if TYPE_CHECKING:
    from api.models.db.key_result import KeyResult
    from api.models.db.user import User


class KeyResultCheckIn(Base):
    __tablename__ = 'key_result_check_in'
    id: Mapped[str] = mapped_column(primary_key=True, nullable=False)
    comment: Mapped[str] = mapped_column()
    value: Mapped[float] = mapped_column()

    user_id: Mapped[str] = mapped_column(ForeignKey('user.id'))
    user: Mapped['User'] = relationship(
        back_populates='key_result_check_ins')

    key_result_id: Mapped[str] = mapped_column(ForeignKey('key_result.id'))
    key_result: Mapped['KeyResult'] = relationship(
        back_populates='key_result_check_ins')

    @property
    def team_id(self):
        return self.key_result.team_id

    @property
    def team(self):
        return self.key_result.team
