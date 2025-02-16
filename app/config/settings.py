from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    APP_NAME: str = "FastAPI App"
    DEBUG: bool
    DATABASE_URL: str

    class Config:
        env = os.getenv("ENV")
        print("HERE", env)

        env_vars = os.environ.keys()
        print(list(env_vars))

        print(os.getenv)

        env_file = None if env == "production" else f"app/config/.env.{env}"
        
settings = Settings()
