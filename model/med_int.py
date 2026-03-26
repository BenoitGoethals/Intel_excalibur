from typing import List
from pydantic import BaseModel


class MedInt(BaseModel):
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
