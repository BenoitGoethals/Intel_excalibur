from typing import List
from pydantic import BaseModel
from model.enums import MasIntType


class MasInt(BaseModel):
    mas_int_type: MasIntType = MasIntType.ACINT
    measurement_type: str = ""
    measurement_value: float = 0.0
    measurement_unit: str = ""
    signature_analysis: str = ""
    target_name: str = ""
    target_location: str = ""
    latitude: float = 0.0
    longitude: float = 0.0
    weather_conditions: str = ""
    atmospheric_conditions: str = ""
    analysis: str = ""
    findings: str = ""
    recommendations: List[str] = []
