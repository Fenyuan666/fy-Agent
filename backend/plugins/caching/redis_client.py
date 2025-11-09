"""Redis client initialisation with lazy loading."""

from __future__ import annotations

from typing import Optional

from backend.core.config import settings

try:  # redis is optional; only import when needed
    from redis.asyncio import Redis
except ImportError as exc:  # pragma: no cover - only executed if redis missing
    Redis = None  # type: ignore
    _import_error = exc
else:
    _import_error = None


redis_client: Optional["Redis"] = None


def init_redis() -> Optional["Redis"]:
    """Initialise the Redis client if configuration is provided."""

    global redis_client
    if not settings.REDIS_URI:
        return None

    if Redis is None:
        raise RuntimeError("redis package is required for caching plugin") from _import_error

    if redis_client is None:
        redis_client = Redis.from_url(settings.REDIS_URI, decode_responses=True)
    return redis_client


async def close_redis() -> None:
    if redis_client is not None:
        await redis_client.aclose()
