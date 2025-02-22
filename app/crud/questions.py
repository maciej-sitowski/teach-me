from app.pagination import PaginatedResponse
from sqlmodel import Session, select
from app.models.questions import Question
from fastapi_pagination import paginate
import sqlalchemy


def create_question(session: Session, question: Question) -> Question:
    """Create a new question and save it to the database"""
    session.add(question)
    session.commit()
    session.refresh(question)
    return question


def get_questions(session: Session) -> list[Question]:
    statement = select(Question).order_by(Question.created_at)
    results = session.exec(statement).all()
    return paginate(results)


def search_questions(session: Session, search_text: str) -> list[Question]:
    statement = select(Question).where(
        Question.title.ilike(f"%{search_text}%") | Question.answer.ilike(f"%{search_text}%")
    ).order_by(Question.created_at)
    results = session.exec(statement).all()
    return paginate(results)


def get_question(session: Session, question_id: int) -> Question:
    # Fetch the question by ID
    question = session.get(Question, question_id)
    if not question:
        raise ValueError(f"Question with id {question_id} not found")
    return question


def update_question(session: Session, question_id: int, updated_data: dict) -> Question:
    # Fetch the question by ID
    question = session.get(Question, question_id)
    if not question:
        raise ValueError(f"Question with id {question_id} not found")
    
    # Update fields based on the provided data
    for key, value in updated_data.items():
        setattr(question, key, value)

    # Save changes to the database
    session.add(question)
    session.commit()
    session.refresh(question)
    return question


def delete_question(session: Session, question_id: int) -> Question:
    # Fetch the question by ID
    question = session.get(Question, question_id)
    if not question:
        raise ValueError(f"Question with id {question_id} not found")
    
    # Save changes to the database
    session.delete(question)
    session.commit()
    session.refresh(question)
    return question


def get_random_question(session: Session) -> Question:
    statement = select(Question).order_by(sqlalchemy.func.random()).limit(1)
    result = session.exec(statement).first()
    if not result:
        raise ValueError("No questions available")
    return result