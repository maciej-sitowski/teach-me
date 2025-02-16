import os
from sqlmodel import create_engine, Session
from .config.settings import settings


engine = create_engine(settings.DATABASE_URL)


# Dependency to get a database session
def get_session():
    with Session(engine) as session:
        yield session
