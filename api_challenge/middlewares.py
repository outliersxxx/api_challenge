# -*- coding: utf-8 -*-
"""Middlewares para las requsts de la API."""

import uuid

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request

from api_challenge import RUN_IDS


def register_run_id_middleware(app: FastAPI):
    """Registra middleware de run id en la aplicación."""

    @app.middleware("http")
    async def run_id_middleware(  # pylint: disable=unused-variable
        request: Request, call_next
    ):
        """Asigna un run id globales a cada request.

        See Also: `hermes.typehints.State`

        """

        request.state.request_globals = RUN_IDS
        response = await call_next(request)

        return response


def register_uuid_middleware(app: FastAPI):
    """Registra middleware uuid en la aplicación."""

    @app.middleware("http")
    async def uuid_middleware(  # pylint: disable=unused-variable
        request: Request, call_next
    ):
        """Asigna un UUID a cada request."""

        request_locals = {
            "uuid": str(uuid.uuid4()),
            "url": str(request.url),
            "request": dict(request),
        }
        request.state.request_locals = request_locals
        response = await call_next(request)

        return response


def register_middlewares(app: FastAPI):
    """Registra varios middlewares en la aplicación."""

    register_run_id_middleware(app)
    register_uuid_middleware(app)
