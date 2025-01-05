from pydantic import BaseModel, Field

class QueryInput(BaseModel):
    question: str
    space: str
    page_id: list = Field(default=None)
