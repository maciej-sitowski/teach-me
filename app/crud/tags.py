from sqlmodel import Session, select
from app.models.tags import Tag
from fastapi_pagination import paginate


def get_tags(session: Session) -> list[Tag]:
    """Fetch all tags from the database"""
    statement = select(Tag).order_by(Tag.name)
    results = session.exec(statement).all()
    return paginate(results)


def get_tag(session: Session, tag_id: int) -> Tag:
    # Fetch the question by ID
    tag = session.get(Tag, tag_id)
    if not tag:
        raise ValueError(f"Tag with id {tag_id} not found")
    return tag


def create_tag(session: Session, tag: Tag) -> Tag:
    """Create a new tag and save it to the database"""
    session.add(tag)
    session.commit()
    session.refresh(tag)
    return tag


def update_tag(session: Session, tag_id: int, updated_data: dict) -> Tag:
    # Fetch the question by ID
    tag = session.get(Tag, tag_id)
    if not tag:
        raise ValueError(f"Tag with id {tag_id} not found")
    
    # Update fields based on the provided data
    for key, value in updated_data.items():
        setattr(tag, key, value)

    # Save changes to the database
    session.add(tag)
    session.commit()
    session.refresh(tag)
    return tag


def delete_tag(session: Session, tag_id: int) -> Tag:
    statement = select(Tag).where(Tag.id == tag_id)
    result = session.exec(statement).first()

    if not result:
        raise ValueError(f"Tag with id {tag_id} not found")

    session.delete(result)
    session.commit()

    return {"detail": "Tag deleted successfully"}