# -*- coding: utf-8 -*-
"""Search routes."""

from textwrap import dedent as _
from typing import Optional

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Path
from fastapi import Query
from pydantic import BaseModel

router = APIRouter()  # pylint: disable=invalid-name,

class Josito(BaseModel):
    name: str
    price: float

def model(price: float):
    return 2*price


@router.post("/predict/")
async def predict_model(
    josito: Josito
):
    """Predicción de modelo"""

    # Logica del modelo

    # Transformar josito para un input de modelo adecuado
    prediction = model(josito.price)
    result = {"prediction": prediction, "name": josito.name}
    return result
