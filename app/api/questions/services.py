# services/question_service.py
from sqlalchemy.ext.asyncio import AsyncSession
from .models import Question
from .schemas import QuestionCreate

async def create_question(question_data: QuestionCreate, db: AsyncSession):
    new_question = Question(**question_data.model_dump())
    db.add(new_question)
    await db.commit()
    await db.refresh(new_question)
    return new_question
