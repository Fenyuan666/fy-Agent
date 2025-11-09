"""FastAPI dependencies exposed by the auth plugin."""

from fastapi import Depends, Header, HTTPException, status

from .models import UserPublic
from .services import InMemoryUserService, user_service


def get_user_service() -> InMemoryUserService:
    """Expose the user service for other plugins."""

    return user_service


def get_current_user(
    x_user_email: str = Header(..., alias="X-User-Email"),
    service: InMemoryUserService = Depends(get_user_service),
) -> UserPublic:
    """Retrieve the user associated with the request."""

    user = service.get_user(x_user_email)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid user")
    return user
