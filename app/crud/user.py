from sqlmodel import Session, select
from app.models.user import User
from app.security import hash_password
from fastapi import HTTPException


def get_user_by_username(session: Session, username: str):
    statement = select(User).where(User.username == username)
    return session.exec(statement).first()


def create_user(session: Session, username: str, password: str):
    hashed_password = hash_password(password)
    user = User(username=username, hashed_password=hashed_password)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def get_users(session: Session):
    users = session.query(User).all()
    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    return users