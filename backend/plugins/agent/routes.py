from __future__ import annotations

"""Agent API endpoints."""

from typing import Any, Optional

from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field

from .services import AgentService, get_agent_service

try:  # Auth integration is optional
    from backend.plugins.auth.deps import get_current_user  # type: ignore
    from backend.plugins.auth.models import UserPublic  # type: ignore
except ImportError:  # pragma: no cover - fallback for disabled auth
    UserPublic = Any  # type: ignore[assignment]
    user_dependency = None
else:
    user_dependency = Depends(get_current_user)  # type: ignore[arg-type]


class AgentRequest(BaseModel):
    prompt: str = Field(..., description="User instruction for the agent")
    context: dict[str, Any] | None = None
    engine_name: str | None = None


class AgentResponse(BaseModel):
    answer: str
    engine: str


router = APIRouter()


@router.post("/ask", response_model=AgentResponse)
async def ask_agent(
    payload: AgentRequest,
    service: AgentService = Depends(get_agent_service),
    user: Optional[UserPublic] = user_dependency,  # type: ignore[arg-type]
) -> AgentResponse:
    context = payload.context or {}
    if user:
        context.setdefault("user_id", user.id)

    result = await service.ask(prompt=payload.prompt, context=context, engine_name=payload.engine_name)
    return AgentResponse(answer=result, engine=payload.engine_name or "default")
