from datetime import datetime
from typing import List
from uuid import uuid4
from pydantic import BaseModel, Field


class ImInt(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    case_id: Optional[str] = None  # 0..1 link to IntelCase
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
