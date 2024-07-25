import uuid
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship


from .base import Base


class User(Base):
    __tablename__ = 'user'
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, nullable=False)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)

    key_results = relationship('KeyResult', back_populates='user')
    key_result_check_ins = relationship(
        'KeyResultCheckIn', back_populates='user')
    key_result_check_marks = relationship(
        'KeyResultCheckMark', back_populates='assigned_user')
    key_result_comments = relationship(
        'KeyResultComment', back_populates='user')
