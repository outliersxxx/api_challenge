# -*- coding: utf-8 -*-
"""Registro de rutas."""

from fastapi import FastAPI


def register_routes(app: FastAPI):
    """Registra las rutas versionadas de la API."""

    from api_challenge.api import api_router as v1

    routers = {
        "v1": v1,
        # TODO agregar las rutas acá
    }
    for version, router in routers.items():
        app.include_router(router, prefix=f"/api/{version}")

