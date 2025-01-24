from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = 'sqlite:///./quiz.db'
    SECRET_KEY: str = "your-secret-key"

    class Config:
        env_file = '.env'

settings = Settings()