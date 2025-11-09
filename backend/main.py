"""Entrypoint for running the FastAPI app with uvicorn."""

from backend.core import create_app

app = create_app()
