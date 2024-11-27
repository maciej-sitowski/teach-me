from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from app.database import get_session
from app.schemas.user import UserCreate, UserResponse
from app.crud.user import create_user, get_user_by_username, get_users


router = APIRouter(prefix="/users", tags=["User"])


@router.get("/", response_model=List[UserResponse])
def get_all_users(session: Session = Depends(get_session)):
    """Retrieve all users."""
    return get_users(session)


@router.post("/register", response_model=UserResponse)
def register(user_data: UserCreate, session: Session = Depends(get_session)):
    if get_user_by_username(session, user_data.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists",
        )
    new_user = create_user(session, user_data.username, user_data.password)
    return new_user

