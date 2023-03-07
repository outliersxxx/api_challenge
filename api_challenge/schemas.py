import enum
from typing import List
from pydantic import BaseModel


class Month(enum.Enum):
    jan = 1
    feb = 2
    mar = 3
    apr = 4
    may = 5
    jun = 6
    jul = 7
    aug = 8
    sep = 9
    oct = 10
    nov = 11
    dic = 12


class FlyType(str, enum.Enum):
    national = "N"
    international = "I"


class Features(BaseModel):
    OPERA: str
    TIPOVUELO: FlyType
    MES: Month

    class Config:
        use_enum_values = True


class ModelInput(BaseModel):
    features: List[Features]

    class Config:
        use_enum_values = True


class ModelOutput(BaseModel):
    prediction: List[int]
