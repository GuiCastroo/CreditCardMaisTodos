import os

import dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

dotenv.load_dotenv()


class Settings(BaseSettings):

    model_config = SettingsConfigDict(case_sensitive=True)
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    DB_URL: str = os.getenv("DB_URL")
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30)
    DB_URL_ALEMBIC: str = os.getenv("DB_URL_ALEMBIC")


settings = Settings()
