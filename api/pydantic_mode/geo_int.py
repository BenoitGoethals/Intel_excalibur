from typing import List
from uuid import uuid4
from pydantic import BaseModel, Field


class GeoInt(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    case_id: Optional[str] = None  # 0..1 link to IntelCase
    target_location: str = ""
    latitude: float = 0.0
    longitude: float = 0.0
    imagery_sources: List[str] = []
    maps: List[str] = []
    terrain_description: str = ""
    infrastructure_details: List[str] = []
    weather_conditions: str = ""
    natural_hazards: str = ""
    analysis: str = ""
    interpretation: str = ""
    recommendations: List[str] = []
