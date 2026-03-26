from datetime import datetime
from typing import List
from uuid import uuid4
from pydantic import BaseModel, Field


class GovSource(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    case_id: Optional[str] = None  # 0..1 link to IntelCase
    source_name: str = ""
    source_type: str = ""
    source_agency: str = ""
    reliability_rating: int = 0
    clearance_level: str = ""
    contact_name: str = ""
    contact_title: str = ""
    contact_phone_number: str = ""
    contact_email: str = ""
    intelligence_contributions: List[str] = []
    operational_status: str = ""
    last_contact_date: datetime = datetime.min
