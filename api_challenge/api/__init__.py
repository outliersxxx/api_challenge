# -*- coding: utf-8 -*-
"""API first version."""

from fastapi import APIRouter

from api_challenge.api import model_predict


api_router = APIRouter()  # pylint: disable=invalid-name,

api_router.include_router(model_predict.router, tags=["Model"])
