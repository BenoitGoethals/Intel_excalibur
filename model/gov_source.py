from datetime import datetime
from typing import List
from pydantic import BaseModel


class GovSource(BaseModel):
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
