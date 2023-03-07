# coding=utf-8

from pathlib import Path

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Configuraciones desde variables de entorno."""

    PROJECT_PATH: Path = Path(__file__).parent.parent

    PACKAGE_PATH: Path = Path(__file__).parent

    MODEL_ENVIRONMENTS_PATH: Path = PROJECT_PATH / "model_environments"

    API_HOST: str = "0.0.0.0"
    """Host para montar la API."""

    API_PORT: int = 5000
    """Puerto para montar la API."""
