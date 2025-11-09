"""Auth plugin API routes."""

from fastapi import APIRouter, Depends, HTTPException, status

from .deps import get_current_user, get_user_service
from .models import TokenPayload, UserCreate, UserLogin, UserPublic
from .services import InMemoryUserService

router = APIRouter()


@router.post("/register", response_model=UserPublic)
async def register_user(
    payload: UserCreate,
    service: InMemoryUserService = Depends(get_user_service),
) -> UserPublic:
    """Register a new user account."""

    try:
        return service.register(payload)
    except ValueError as exc:  # pragma: no cover - illustrative branch
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.post("/login", response_model=TokenPayload)
async def login(
    payload: UserLogin,
    service: InMemoryUserService = Depends(get_user_service),
) -> TokenPayload:
    token = service.authenticate(payload)
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return token


@router.get("/me", response_model=UserPublic)
async def read_current_user(user: UserPublic = Depends(get_current_user)) -> UserPublic:
    return user
