from sqlalchemy.ext.asyncio import AsyncSession
from .models import Quiz
from .schemas import QuizCreate

async def create_quiz(quiz_data: QuizCreate, db: AsyncSession):
    # Convert Pydantic model to dictionary and create a new Quiz instance
    new_quiz = Quiz(**quiz_data.model_dump())
    db.add(new_quiz)
    await db.commit()  # Commit the transaction
    await db.refresh(new_quiz)  # Refresh to get the updated instance with its ID
    return new_quiz
