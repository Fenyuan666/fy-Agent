from __future__ import annotations

"""RBAC plugin endpoints."""

from typing import Any

from fastapi import APIRouter, Depends

from .models import Role, RoleAssignment
from .services import InMemoryRBACService, rbac_service

try:  # Optional auth integration
    from backend.plugins.auth.deps import get_current_user  # type: ignore
    from backend.plugins.auth.models import UserPublic  # type: ignore
except ImportError:  # pragma: no cover - fallback for disabled auth
    from fastapi import HTTPException, status

    def get_current_user():  # type: ignore
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Auth plugin disabled")

    UserPublic = Any  # type: ignore

router = APIRouter()


def get_rbac_service() -> InMemoryRBACService:
    return rbac_service


@router.get("/roles", response_model=list[Role])
async def list_roles(service: InMemoryRBACService = Depends(get_rbac_service)) -> list[Role]:
    return service.list_roles()


@router.post("/roles", response_model=Role)
async def create_role(role: Role, service: InMemoryRBACService = Depends(get_rbac_service)) -> Role:
    return service.upsert_role(role)


@router.post("/assignments", response_model=RoleAssignment)
async def create_assignment(
    assignment: RoleAssignment,
    user: UserPublic = Depends(get_current_user),  # type: ignore[arg-type]
    service: InMemoryRBACService = Depends(get_rbac_service),
) -> RoleAssignment:
    # In a real service you would ensure the acting user is allowed to assign roles.
    service.assign_role(assignment)
    return assignment


@router.get("/assignments", response_model=list[RoleAssignment])
async def list_assignments(
    user: UserPublic = Depends(get_current_user),  # type: ignore[arg-type]
    service: InMemoryRBACService = Depends(get_rbac_service),
) -> list[RoleAssignment]:
    return service.list_assignments(user_id=user.id)
