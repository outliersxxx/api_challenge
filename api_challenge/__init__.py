# -*- coding: utf-8 -*-
"""Setting and get up API"""

import uuid
from socket import gethostname
from fastapi import FastAPI
from starlette.responses import RedirectResponse

from api_challenge.settings import Settings

SETTINGS = Settings()

RUN_IDS = {
    "api_challenge.run_id": str(uuid.uuid4()),
    "api_challenge.host": gethostname(),
    "api_challenge.version": "0.1.0",
}


def make_app():
    """Construye aplicación FastAPI."""

    from api_challenge.middlewares import register_middlewares
    from api_challenge.routes import register_routes

    app = FastAPI(
        title="api_challenge",
        description="Test para Neuralworks",
        version="0.1.0",
        docs_url="/",
    )

    register_middlewares(app)
    register_routes(app)

    return app
