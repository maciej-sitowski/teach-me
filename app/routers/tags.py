from app.crud.tags import create_tag, delete_tag, get_tag, get_tags, update_tag
from app.models.tags import Tag
from fastapi import Depends, HTTPException
from app.database import get_session
from sqlmodel import Session
from fastapi import APIRouter
from fastapi_pagination import Page


router = APIRouter(prefix="/tags", tags=["Tags"])


@router.get("/", response_model=Page[Tag])
def read_all_tags(session: Session = Depends(get_session)):
    return get_tags(session)


@router.get("/{tag_id}")
def read_tag(tag_id: int, session: Session = Depends(get_session)):
    return get_tag(session, tag_id)


@router.post("/")
def create_new_tag(tag: Tag, session: Session = Depends(get_session)):
    return create_tag(session, tag)


@router.put("/{tag_id}", response_model=Tag)
def update_tag_endpoint(
    tag_id: int,
    updated_tag: dict,
    session: Session = Depends(get_session),
):
    try:
        question = update_tag(session, tag_id, updated_tag)
        return question
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/{tag_id}")
def remove_tag(tag_id: int, session: Session = Depends(get_session)):
    return delete_tag(session, tag_id)


