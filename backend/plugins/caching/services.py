"""Caching helpers built on top of Redis."""

from typing import Optional

from .redis_client import init_redis


async def cache_get(key: str) -> Optional[str]:
    client = init_redis()
    if client is None:
        return None
    return await client.get(key)


async def cache_set(key: str, value: str, ttl: int = 60) -> None:
    client = init_redis()
    if client is None:
        return
    await client.set(key, value, ex=ttl)
