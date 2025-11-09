"""Health check endpoint for the service."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/", tags=["health"])  # pragma: no cover - trivial endpoint
async def health_check() -> dict[str, str]:
    """Return a minimal health payload."""

    return {"status": "ok"}
