"""Implementation of authentication service logic."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Optional

from .models import TokenPayload, UserCreate, UserLogin, UserPublic


@dataclass
class InMemoryUserService:
    """Simple in-memory user registry for demos and local development."""

    _users: Dict[str, UserPublic] = field(default_factory=dict)

    def register(self, payload: UserCreate) -> UserPublic:
        if payload.email in self._users:
            raise ValueError("User already exists")

        user = UserPublic(id=payload.email, email=payload.email)
        self._users[payload.email] = user
        return user

    def authenticate(self, payload: UserLogin) -> Optional[TokenPayload]:
        user = self._users.get(payload.email)
        if not user:
            return None

        # NOTE: Replace with proper password hashing & JWT in production.
        if payload.password != "password":
            return None

        return TokenPayload(access_token=f"fake-token-for-{user.id}")

    def get_user(self, email: str) -> Optional[UserPublic]:
        return self._users.get(email)


user_service = InMemoryUserService()
