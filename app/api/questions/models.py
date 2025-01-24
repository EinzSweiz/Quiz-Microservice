from sqlalchemy import Integer, String, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.core.database import Base
from enum import Enum as PyEnum

class QuestionType(str, PyEnum):
    MULTIPLE_CHOICE = "multiple_choice"
    TRUE_FALSE = "true_false"

class Question(Base):
    __tablename__ = 'questions'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    quiz_id: Mapped[int] = mapped_column(ForeignKey('quizzes.id', ondelete="CASCADE"), index=True)
    text: Mapped[str] = mapped_column(String(500), index=True)
    type: Mapped[QuestionType] = mapped_column(Enum(QuestionType), nullable=False)
    choices: Mapped[dict] = mapped_column(JSON, nullable=False)
    correct_answer: Mapped[str] = mapped_column(String(255), nullable=False)

    quiz = relationship('Quiz', back_populates='questions')
