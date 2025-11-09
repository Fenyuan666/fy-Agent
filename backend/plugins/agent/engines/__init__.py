"""Agent engine registry."""

from typing import Dict

from backend.core.config import settings

from .base import AgentEngine, EchoEngine
from .langchain import LangChainEngine

_ENGINE_REGISTRY: Dict[str, AgentEngine] = {}


def get_engine(name: str | None = None) -> AgentEngine:
    """Return a configured agent engine, defaulting to the settings value."""

    key = name or settings.DEFAULT_AGENT_ENGINE
    if key not in _ENGINE_REGISTRY:
        if key == "langchain":
            _ENGINE_REGISTRY[key] = LangChainEngine()
        elif key == "echo":
            _ENGINE_REGISTRY[key] = EchoEngine()
        else:
            raise ValueError(f"Unknown agent engine: {key}")
    return _ENGINE_REGISTRY[key]
