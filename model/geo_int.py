from typing import List
from pydantic import BaseModel


class GeoInt(BaseModel):
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
