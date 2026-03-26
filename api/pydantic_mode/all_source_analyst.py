"""
All-Source Analyst
Combines intelligence from multiple disciplines (HUMINT, SIGINT, OSINT,
GEOINT, MASINT …) into coherent assessments — effectively builds the
"case file" equivalent in the intelligence world.
"""
from typing import List, Optional
from uuid import uuid4
from pydantic import BaseModel, Field


class AllSourceAnalyst(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    case_id: Optional[str] = None  # 0..1 link to IntelCase

    name: str = ""
    rank: Optional[str] = None
    unit: Optional[str] = None
    clearance_level: Optional[str] = None

    # Intelligence disciplines this analyst draws from
    sources_accessed: List[str] = []

    # ID of the current investigation / case file being worked
    current_case_file_id: Optional[str] = None

    # Total finished assessments produced
    assessments_produced: int = 0

    # Methodology used to fuse and weight sources
    fusion_methodology: Optional[str] = None

    # Key subjects or target entities this analyst covers
    target_entities: List[str] = []

    # Analytical tools and systems used
    tools_used: List[str] = []

    # Languages — broadens source material accessible
    languages: List[str] = []

    active: bool = True
    contact_email: Optional[str] = None
    contact_phone: Optional[str] = None
    notes: Optional[str] = None
