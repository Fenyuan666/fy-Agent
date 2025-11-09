"""Redis DB helper that proxies to the caching plugin."""

from backend.plugins.caching.redis_client import init_redis

__all__ = ["init_redis"]
