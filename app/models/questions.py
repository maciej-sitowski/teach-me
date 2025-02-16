from typing import List, TYPE_CHECKING
from app.models.questions_tags import QuestionTag
from app.models.tags import Tag
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime, timezone
from sqlalchemy import Column, String
from app.models.questions_tags import QuestionTag


if TYPE_CHECKING:
    from app.models.tags import Tag


class Question(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str = Field(sa_column=Column(String(500), nullable=False, index=True))  # Correct usage
    answer: str | None = Field(default=None, sa_column=Column(String(1000), nullable=True))  # Correct usage
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    tags: List["Tag"] = Relationship(back_populates="questions", link_model=QuestionTag)
