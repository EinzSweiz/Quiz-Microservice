from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.core.database import Base

class Quiz(Base):
    __tablename__ = 'quizzes'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    questions = relationship('Question', back_populates='quiz', cascade="all, delete-orphan")
