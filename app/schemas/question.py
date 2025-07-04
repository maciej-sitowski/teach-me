from typing import List, Optional
from pydantic import BaseModel

class QuestionCreate(BaseModel):
    title: str
    answer: str
    # Add other fields as needed
    tags: Optional[List[str]] = None
