"""MongoDB connector used by plugins that choose Mongo as backend."""

from __future__ import annotations

from typing import Optional

from backend.core.config import settings

try:  # pragma: no cover - optional dependency
    from motor.motor_asyncio import AsyncIOMotorClient
except ImportError as exc:
    AsyncIOMotorClient = None  # type: ignore
    _import_error = exc
else:
    _import_error = None


_mongo_client: Optional["AsyncIOMotorClient"] = None


def get_mongo_client() -> Optional["AsyncIOMotorClient"]:
    """Return a singleton MongoDB client if configuration allows."""

    global _mongo_client
    if not settings.DATABASE_MONGO_URI:
        return None

    if AsyncIOMotorClient is None:
        raise RuntimeError("motor package is required for MongoDB support") from _import_error

    if _mongo_client is None:
        _mongo_client = AsyncIOMotorClient(settings.DATABASE_MONGO_URI)
    return _mongo_client
