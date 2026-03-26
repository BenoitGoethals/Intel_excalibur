from typing import List
from uuid import uuid4
from pydantic import BaseModel, Field
from api.pydantic_mode.enums import MasIntType


class MasInt(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    case_id: Optional[str] = None  # 0..1 link to IntelCase
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
