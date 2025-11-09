"""RBAC domain models."""

from typing import List

from pydantic import BaseModel, Field


class Permission(BaseModel):
    code: str = Field(..., description="Unique permission code")
    description: str | None = None


class Role(BaseModel):
    name: str
    permissions: List[Permission] = Field(default_factory=list)


class RoleAssignment(BaseModel):
    user_id: str
    role_name: str
