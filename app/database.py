from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "postgresql://myuser:mypassword@localhost/mydatabase"

engine = create_engine(DATABASE_URL)


# Dependency to get a database session
def get_session():
    with Session(engine) as session:
        yield session
