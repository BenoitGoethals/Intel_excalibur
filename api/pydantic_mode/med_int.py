from typing import List
from uuid import uuid4
from pydantic import BaseModel, Field


class MedInt(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    case_id: Optional[str] = None  # 0..1 link to IntelCase
    patient_name: str = ""
    age: int = 0
    gender: str = ""
    diagnosis: str = ""
    symptoms: List[str] = []
    treatments: List[str] = []
    facility_name: str = ""
    facility_location: str = ""
    provider_name: str = ""
    provider_contact: str = ""
    analysis: str = ""
    findings: str = ""
    recommendations: List[str] = []
