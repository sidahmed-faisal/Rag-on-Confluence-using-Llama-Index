from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime


class QueryInput(BaseModel):
    question: str
    space: str
    page_id: list = Field(default=None)
