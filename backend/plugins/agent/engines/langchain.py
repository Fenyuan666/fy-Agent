"""Placeholder LangChain engine integration."""

from typing import Any

from .base import AgentEngine


class LangChainEngine(AgentEngine):
    """Demonstrates how a LangChain backed engine would look."""

    def __init__(self, model_name: str = "gpt-3.5-turbo") -> None:
        self.model_name = model_name

    async def run(self, prompt: str, context: dict[str, Any] | None = None) -> str:
        # Plug LangChain RunnableSequence or AgentExecutor here.
        return f"[LangChain:{self.model_name}] -> {prompt}"
