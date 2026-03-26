from datetime import datetime
from decimal import Decimal
from typing import List
from uuid import uuid4
from pydantic import BaseModel, Field


class TechInt(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    case_id: Optional[str] = None  # 0..1 link to IntelCase
    technology_name: str = ""
    manufacturer: str = ""
    model: str = ""
    technical_specifications: str = ""
    acquisition_source: str = ""
    acquisition_date: datetime = datetime.min
    cost: Decimal = Decimal("0.0")
    usage_history: str = ""
    performance_analysis: str = ""
    compatible_technologies: List[str] = []
    integration_details: str = ""
    analysis: str = ""
    findings: str = ""
    recommendations: List[str] = []
