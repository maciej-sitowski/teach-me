from fastapi import Depends, HTTPException
from app.models.questions import Question
from app.database import get_session
from app.crud.questions import create_question, get_questions, update_question, get_question
from sqlmodel import Session, select
from fastapi import APIRouter
from fastapi_pagination import Page


router = APIRouter(prefix="/questions", tags=["Questions"])


@router.get("/", response_model=Page[Question])
def read_all_questions(session: Session = Depends(get_session)):
    return get_questions(session)


@router.post("/")
def create_new_question(question: Question, session: Session = Depends(get_session)):
    return create_question(session, question)


@router.get("/{question_id}")
def read_one_question(question_id: int, session: Session = Depends(get_session)):
    return get_question(session, question_id)


@router.put("/{question_id}", response_model=Question)
def update_question_endpoint(
    question_id: int,
    updated_question: dict,
    session: Session = Depends(get_session),
):
    try:
        question = update_question(session, question_id, updated_question)
        return question
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/{question_id}", status_code=204)
def delete_question(question_id: int, session: Session = Depends(get_session)):
    # Fetch the question from the database
    statement = select(Question).where(Question.id == question_id)
    result = session.exec(statement).first()

    # Check if the question exists
    if not result:
        raise HTTPException(status_code=404, detail="Question not found")

    # Delete the question
    session.delete(result)
    session.commit()

    return {"detail": "Question deleted successfully"}