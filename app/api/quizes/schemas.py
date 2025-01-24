# schema/quiz_schema.py
from pydantic import BaseModel, Field

class QuizBase(BaseModel):
    title: str = Field(..., max_length=255, description="The quiz title")
    description: str = Field(..., max_length=500, description="The quiz description")

class QuizCreate(QuizBase):
    pass

class QuizResponse(QuizBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True