"""API serving."""

from typing import Optional

import uvicorn

from api_challenge import make_app
from api_challenge import SETTINGS


def serve():
    """Serve API from uvicorn."""

    app = make_app()

    uvicorn.run(
        app,
        host=SETTINGS.API_HOST,
        port=SETTINGS.API_PORT,
    )


if __name__ == "__main__":
    serve()
