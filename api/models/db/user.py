from typing import TYPE_CHECKING, List
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

from api.models.db.base import Base
if TYPE_CHECKING:
    from api.models.db.key_result import KeyResult
    from api.models.db.objective import Objective
from api.models.db.key_result_check_in import KeyResultCheckIn
from api.models.db.key_result_check_mark import KeyResultCheckMark
from api.models.db.key_result_comment import KeyResultComment


class User(Base):
    __tablename__ = 'user'
    id: Mapped[str] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column()
    last_name: Mapped[str] = mapped_column()

    objectives: Mapped[List['Objective']] = relationship(
        back_populates='owner')
    key_results: Mapped[List['KeyResult']
                        ] = relationship(back_populates='owner')
    key_result_check_ins: Mapped[List['KeyResultCheckIn']] = relationship(
        back_populates='user')
    key_result_check_marks: Mapped[List['KeyResultCheckMark']] = relationship(
        back_populates='assigned_user')
    key_result_comments: Mapped[List['KeyResultComment']] = relationship(
        back_populates='user')
