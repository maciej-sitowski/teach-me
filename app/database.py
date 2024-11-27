from sqlmodel import SQLModel, create_engine, Session
import os

# DATABASE_URL = "postgresql://myuser:mypassword@localhost/mydatabase"

DATABASE_URL = f"postgresql://postgres.qtbtxfapbpkvormweems:{os.environ['DATABASE_PASSWORD']}@aws-0-us-east-1.pooler.supabase.com:6543/postgres"

engine = create_engine(DATABASE_URL)


# Dependency to get a database session
def get_session():
    with Session(engine) as session:
        yield session
