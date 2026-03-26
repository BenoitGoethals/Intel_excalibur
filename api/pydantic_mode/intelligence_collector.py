"""
Intelligence Collector
Gathers raw information through direct collection methods:
interrogations, surveillance, reconnaissance, SIGINT intercept, etc.
"""
from datetime import datetime
from typing import List, Optional
from uuid import uuid4
from pydantic import BaseModel, Field


class IntelligenceCollector(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    case_id: Optional[str] = None  # 0..1 link to IntelCase

    name: str = ""
    rank: Optional[str] = None
    unit: Optional[str] = None
    clearance_level: Optional[str] = None

    # Primary collection method: HUMINT / SIGINT / IMINT / OSINT / MASINT …
    collection_method: Optional[str] = None

    # Geographic or target area being collected against
    target_area: Optional[str] = None

    # Specific assets, sensors or platforms used
    collection_assets: List[str] = []

    # Number of active collection operations currently running
    active_operations: int = 0

    # Date of most recent collection mission
    last_collection_date: Optional[datetime] = None

    # Certifications and special qualifications
    qualifications: List[str] = []

    # Languages — critical for HUMINT collectors
    languages: List[str] = []

    active: bool = True
    contact_email: Optional[str] = None
    contact_phone: Optional[str] = None
    notes: Optional[str] = None
