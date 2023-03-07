# -*- coding: utf-8 -*-
"""Search routes."""

from fastapi import APIRouter
from pydantic import BaseModel
import pandas as pd

from api_challenge.read_model import MODELS
from api_challenge.schemas import ModelInput
from api_challenge.schemas import ModelOutput


router = APIRouter()  # pylint: disable=invalid-name,


@router.post("/predict/")
async def predict_model(model_input: ModelInput, name_model: str):
    """Predicción de modelo"""

    prediction = MODELS[name_model](pd.DataFrame(model_input.dict()["features"]))
    prediction = [int(val) for val in prediction]
    return {"predictions": prediction}
