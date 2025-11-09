"""Backend package exposing the application factory."""

from .core.app import create_app

__all__ = ["create_app"]
