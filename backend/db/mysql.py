"""MySQL connector built on SQLAlchemy."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from backend.core.config import settings

_mysql_engine: Optional[Engine] = None


def get_mysql_engine() -> Optional[Engine]:
    global _mysql_engine
    if not settings.DATABASE_MYSQL_URI:
        return None

    if _mysql_engine is None:
        _mysql_engine = create_engine(settings.DATABASE_MYSQL_URI)
    return _mysql_engine
