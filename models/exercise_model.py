from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

from . import Base

if TYPE_CHECKING:
    from models.exercise_model import Exercise

class Exercise(Base):
    pass