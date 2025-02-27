from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

from . import Base

if TYPE_CHECKING:
    from models.workout_model import Workout


class Workout(Base):
    __tablename__ = "workout"

    id: Mapped[int] = mapped_column(autoincrement=True)