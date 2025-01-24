from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional, Dict

class QuestionType(str, Enum):
    MULTIPLE_CHOICE = "multiple_choice"
    TRUE_FALSE = "true_false" 

class QuestionBase(BaseModel):
    text: str = Field(max_length=500,  description="The question text")
    type: QuestionType = Field(description="Type of the question (multiple_choice or true_false)")
    choices: Dict[str, str] = Field(description="Possible answers in a dictionary format")
    correct_answer: str = Field(max_length=255, description="The correct answer to the question")

class QuestionCreate(QuestionBase):
    quiz_id: int = Field(description="The ID of the associated quiz")


class QuestionResponse(QuestionBase):
    id: int
    quiz_id: int

    class Config:
        orm_mode = True