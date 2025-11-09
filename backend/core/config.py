"""Application configuration and feature flags."""

from functools import lru_cache
from typing import Optional

try:  # pydantic v2
    from pydantic_settings import BaseSettings, SettingsConfigDict
except ImportError:  # pragma: no cover - fallback for pydantic v1
    from pydantic import BaseSettings  # type: ignore
    SettingsConfigDict = None  # type: ignore


class Settings(BaseSettings):
    """Centralised settings with feature toggles for backend services."""

    PROJECT_NAME: str = "fy-agent Framework"
    API_PREFIX: str = "/api/v1"

    FEATURE_AUTH: bool = True
    FEATURE_RBAC: bool = False
    FEATURE_AGENT: bool = True
    FEATURE_REDIS: bool = False

    AUTH_DATABASE_BACKEND: str = "mongo"  # mongo | mysql
    RBAC_DATABASE_BACKEND: str = "mysql"  # mysql | mongo

    DATABASE_MONGO_URI: Optional[str] = None
    DATABASE_MYSQL_URI: Optional[str] = None
    REDIS_URI: Optional[str] = None

    # Optional external services
    DEFAULT_AGENT_ENGINE: str = "echo"

    if SettingsConfigDict is not None:  # pragma: no branch
        model_config = SettingsConfigDict(
            env_file=".env",
            env_file_encoding="utf-8",
            case_sensitive=False,
        )

    class Config:  # type: ignore[override]
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


@lru_cache
def get_settings() -> Settings:
    """Return a cached Settings instance."""

    return Settings()  # type: ignore[arg-type]


settings = get_settings()
