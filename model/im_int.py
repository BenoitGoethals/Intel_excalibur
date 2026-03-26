from datetime import datetime
from typing import List
from pydantic import BaseModel


class ImInt(BaseModel):
    image_name: str = ""
    image_source: str = ""
    capture_date: datetime = datetime.min
    image_format: str = ""
    target_name: str = ""
    target_location: str = ""
    latitude: float = 0.0
    longitude: float = 0.0
    image_analysis: str = ""
    key_features: List[str] = []
    interpretation: str = ""
    findings: str = ""
    recommendations: List[str] = []
