from pydantic import BaseSettings


class Settings(BaseSettings):
    IS_LIVE: bool = False
    SQLALCHEMY_DATABASE_URI: str


settings = Settings()
