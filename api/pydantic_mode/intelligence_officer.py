"""
Intelligence Officer (S2 / G2 / J2)
Responsible for all intelligence activities within a unit.
  Battalion level  → S2
  Brigade/Division → G2
  Joint/Combined   → J2
  Naval            → N2
  Air Force        → A2
"""
from typing import List, Optional
from uuid import uuid4
from pydantic import BaseModel, Field


class IntelligenceOfficer(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    case_id: Optional[str] = None  # 0..1 link to IntelCase

    name: str = ""
    rank: Optional[str] = None

    # S2 / G2 / J2 / N2 / A2
    designation: str = "S2"

    unit: Optional[str] = None
    clearance_level: Optional[str] = None

    # The geographic or functional area this officer is responsible for
    area_of_responsibility: Optional[str] = None

    # Officers this S2/G2/J2 directs
    subordinate_analysts: int = 0

    # The senior officer this role reports to
    reporting_to: Optional[str] = None

    # Current overall intelligence assessment for the AO
    current_assessment: Optional[str] = None

    # Priority Intelligence Requirements (PIRs)
    intelligence_priorities: List[str] = []

    # Standing intelligence products this officer owns
    intelligence_products: List[str] = []

    active: bool = True
    contact_email: Optional[str] = None
    contact_phone: Optional[str] = None
    notes: Optional[str] = None
