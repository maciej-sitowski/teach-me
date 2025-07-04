from fastapi import Depends, HTTPException
from app.models.questions import Question
from app.database import get_session
from app.crud.questions import create_question, get_questions, get_random_question, search_questions, update_question, get_question
from sqlmodel import Session, select
from fastapi import APIRouter
from fastapi_pagination import Page
from app.models.questions_tags import QuestionTag
from sqlalchemy.sql.expression import func
from app.models.tags import Tag
from app.schemas.question import QuestionCreate
from app.models.questions import Question


router = APIRouter(prefix="/questions", tags=["Questions"])


@router.get("/", response_model=Page[Question])
def read_all_questions(session: Session = Depends(get_session)):
    return get_questions(session)


@router.post("/")
def create_new_question(question: QuestionCreate, session: Session = Depends(get_session)):
    # Create the question (excluding tags)
    db_question = Question(
        title=question.title,
        answer=question.answer
    )  # Add other fields as needed
    session.add(db_question)
    session.commit()
    session.refresh(db_question)
    # Handle tags if provided
    if question.tags:
        for tag_name in question.tags:
            tag_obj = session.exec(select(Tag).where(Tag.name == tag_name)).first()
            if tag_obj:
                question_tag = QuestionTag(question_id=db_question.id, tag_id=tag_obj.id)
                session.add(question_tag)
    session.commit()
    return db_question


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


@router.get("/search/", response_model=Page[Question])
def search_questions_endpoint(search_text: str, session: Session = Depends(get_session)):
    return search_questions(session, search_text)


@router.get("/random/", response_model=Question)
def get_random_question_endpoint(tag: str = None, session: Session = Depends(get_session)):
    if tag is not None:
        tag_obj = session.exec(select(Tag).where(Tag.name == tag)).first()
        if not tag_obj:
            raise HTTPException(status_code=404, detail="Tag not found")
        tag_id = tag_obj.id
        statement = (
            select(Question)
            .join(QuestionTag, Question.id == QuestionTag.question_id)
            .where(QuestionTag.tag_id == tag_id)
            .order_by(func.random())
            .limit(1)
        )
        question = session.exec(statement).first()
        if not question:
            raise HTTPException(status_code=404, detail="No question found for this tag")
        return question
    try:
        question = get_random_question(session)
        return question
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/{question_id}/tags/{tag_id}")
def add_tag_to_question(question_id: int, tag_id: int, session: Session = Depends(get_session)):
    # Check if the association already exists
    existing = session.exec(
        select(QuestionTag).where(
            (QuestionTag.question_id == question_id) & (QuestionTag.tag_id == tag_id)
        )
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="Tag already added to question")
    # Create the association
    question_tag = QuestionTag(question_id=question_id, tag_id=tag_id)
    session.add(question_tag)
    session.commit()
    session.refresh(question_tag)
    return {"detail": "Tag added to question"}