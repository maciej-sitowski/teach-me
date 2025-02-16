from typing import List, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column, String
from app.models.questions_tags import QuestionTag


if TYPE_CHECKING:
    from app.models.questions import Question


class Tag(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(sa_column=Column(String(50), nullable=False, unique=True))
    questions: List["Question"] = Relationship(back_populates="tags", link_model=QuestionTag)