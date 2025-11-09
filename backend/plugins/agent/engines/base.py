"""Base protocol for agent engines."""

from typing import Any, Protocol


class AgentEngine(Protocol):
    async def run(self, prompt: str, context: dict[str, Any] | None = None) -> str:
        """Execute an agent prompt and return the response."""


class EchoEngine:
    """Fallback engine that simply echoes the user prompt."""

    async def run(self, prompt: str, context: dict[str, Any] | None = None) -> str:  # pragma: no cover - trivial
        return f"Echo: {prompt}"
