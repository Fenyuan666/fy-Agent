"""Application factory that wires all optional plugins based on configuration."""

from fastapi import FastAPI

from .config import settings
from .health import router as health_router


def create_app() -> FastAPI:
    """Instantiate the FastAPI app and register enabled plugins."""

    app = FastAPI(title=settings.PROJECT_NAME)

    # Core routes
    app.include_router(health_router, prefix="/health")

    # Optional plugin routes
    if settings.FEATURE_AUTH:
        from backend.plugins.auth.routes import router as auth_router

        app.include_router(auth_router, prefix=f"{settings.API_PREFIX}/auth", tags=["auth"])

    if settings.FEATURE_RBAC:
        from backend.plugins.rbac.routes import router as rbac_router

        app.include_router(rbac_router, prefix=f"{settings.API_PREFIX}/rbac", tags=["rbac"])

    if settings.FEATURE_AGENT:
        from backend.plugins.agent.routes import router as agent_router

        app.include_router(agent_router, prefix=f"{settings.API_PREFIX}/agent", tags=["agent"])

    if settings.FEATURE_REDIS:
        from backend.plugins.caching.redis_client import init_redis

        init_redis()

    return app
