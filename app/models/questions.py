from sqlmodel import SQLModel, Field
from datetime import datetime, timezone
from sqlalchemy import Column, String


class Question(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str = Field(sa_column=Column(String(500), nullable=False, index=True))  # Correct usage
    answer: str | None = Field(default=None, sa_column=Column(String(1000), nullable=True))  # Correct usage
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))