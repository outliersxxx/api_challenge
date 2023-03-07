import cloudpickle
from typing import Callable

from api_challenge import SETTINGS


class ModelReader:
    def __init__(self, model_name):
        self.model_name = model_name
        self._model = None

    @property
    def model(self) -> Callable:
        if self._model is None:
            try:
                with open(
                    SETTINGS.MODEL_ENVIRONMENTS_PATH / f"{self.model_name}.pkl", "rb"
                ) as file:
                    model = cloudpickle.load(file)
                self._model = model
            except Exception as exc:
                print("No es posible cargar el ambiente de los modelos")
                raise exc
        return self._model


MODELS = {
    "logistic_model": ModelReader("logistic_model").model,
    "xgboost_model": ModelReader("xgboost_model").model,
    "catboost_model": ModelReader("catboost_model").model,
    "xgboost_fI_model": ModelReader("xgboost_fI_model").model,
    "catboost_fI_model": ModelReader("catboost_fI_model").model,
}
