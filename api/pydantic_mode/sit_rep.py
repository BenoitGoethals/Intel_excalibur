from datetime import datetime
from typing import List
from uuid import uuid4
from pydantic import BaseModel, Field


class SitRep(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    case_id: Optional[str] = None  # 0..1 link to IntelCase
    report_date_time: datetime = datetime.min
    reporting_unit: str = ""
    location: str = ""
    enemy_disposition: str = ""
    enemy_capabilities: str = ""
    friendly_disposition: str = ""
    friendly_capabilities: str = ""
    civilian_considerations: str = ""
    weather_conditions: str = ""
    terrain_analysis: str = ""
    other_information: List[str] = []
    recommendations: str = ""
    future_plans: str = ""
