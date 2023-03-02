"""API serving."""

from typing import Optional

import uvicorn

from api_challenge import make_app

DEFAULT_UVICORN_HOST = "0.0.0.0"
"""Setting to 0.0.0.0, means any incoming connections are acceptable."""

DEFAULT_API_PORT = 5000


def serve():
    """Serve API from uvicorn."""

    app = make_app()

    uvicorn.run(
        app,
        host=DEFAULT_UVICORN_HOST,
        port=DEFAULT_API_PORT,

    )


if __name__ == "__main__":
    serve()
