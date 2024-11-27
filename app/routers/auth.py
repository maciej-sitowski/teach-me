from fastapi import APIRouter, Depends, HTTPException, Form
from sqlmodel import Session
from app.database import get_session
from app.schemas.user import Token
from app.crud.user import get_user_by_username
from app.security import verify_password, create_access_token


router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login", response_model=Token)
def login(
    username: str = Form(...),  # Form data
    password: str = Form(...),  # Form data
    session: Session = Depends(get_session),
):
    user = get_user_by_username(session, username)
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}