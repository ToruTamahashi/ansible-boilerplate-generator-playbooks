from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_ENV: str = "production"
    DATABASE_URI: str = "sqlite:"

    class Config:
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
