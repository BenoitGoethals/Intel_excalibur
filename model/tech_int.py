from datetime import datetime
from decimal import Decimal
from typing import List
from pydantic import BaseModel


class TechInt(BaseModel):
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
