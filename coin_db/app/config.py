import logging
from functools import lru_cache

from pydantic import BaseSettings, Field

log = logging.getLogger(__name__)


class Settings(BaseSettings):
    ENVIRONMENT: str = Field(...)
    WEB_APP_TITLE: str = Field(...)
    WEB_APP_DESCRIPTION: str = Field(...)
    WEB_APP_VERSION: str = Field(...)
    DEFAULT_EXPIRE_TIME: int = Field(...)

    POSTGRES_DATABASE_URL: str = Field(...)


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings: Settings = get_settings()
