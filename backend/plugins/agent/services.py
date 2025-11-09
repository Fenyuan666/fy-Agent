"""Agent service orchestrating engine calls."""

from typing import Any, Optional

from .engines import get_engine


class AgentService:
    async def ask(
        self,
        prompt: str,
        context: Optional[dict[str, Any]] = None,
        engine_name: str | None = None,
    ) -> str:
        engine = get_engine(engine_name)
        return await engine.run(prompt, context)


agent_service = AgentService()


def get_agent_service() -> AgentService:
    return agent_service
