from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.responses import Response, JSONResponse
from pydantic import BaseModel, Field, ConfigDict, EmailStr
from .api.quizes.models import Quiz
from .api.questions.services import create_question
from .api.quizes.services import create_quiz
from typing import Annotated
from .core.database import setup_database, get_session
from .api.quizes.schemas import QuizCreate
from sqlalchemy.ext.asyncio import AsyncSession
from .api.questions.schemas import QuestionCreate
# from app.api.routes.quize_routes import quiz_routes
# from app.api.routes.question_routes import question_router

app = FastAPI(title='Quiz Microservice', version='1.0')

SessionDep = Annotated[AsyncSession, Depends(get_session)]
# app.include_router(quiz_routes, prefix='/quizzes', tags=['Quizzes'])
# app.include_router(question_router, prefix='/questions', tags=['Questions'])

@app.get('/', tags=['Main API'], summary='Main API')
def root():
    return {"message": "Welcome to the Quiz Microservice"}

@app.post('/setup/databse', tags=['Just Example'], summary='example with db')
async def activate_db():
    try:
        await setup_database()
        return JSONResponse({'success': 'Database successfully restarted'}, status_code=status.HTTP_202_ACCEPTED)
    except Exception as e:
        return JSONResponse({'error': str(e)}, status_code=status.HTTP_400_BAD_REQUEST)


@app.post('/quiz/create', response_model=QuizCreate)
async def create_quiz_api(
    quiz: QuizCreate, session: SessionDep
):
    return await create_quiz(quiz, session)

@app.post('/question/create', response_model=QuestionCreate)
async def create_question_api(
    question: QuestionCreate, session: SessionDep
):
    quiz = await session.get(Quiz, question.quiz_id)
    if not quiz:
        raise JSONResponse({'error': 'Quiz not found'}, status_code=status.HTTP_400_BAD_REQUEST)
    return await create_question(question, session)
