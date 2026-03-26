"""
Intelligence Analyst
Processes and analyses collected information (HUMINT, SIGINT, OSINT, GEOINT …)
and produces finished intelligence reports.
"""
from typing import List, Optional
from uuid import uuid4
from pydantic import BaseModel, Field


class IntelligenceAnalyst(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    case_id: Optional[str] = None  # 0..1 link to IntelCase

    name: str = ""
    rank: Optional[str] = None
    unit: Optional[str] = None
    clearance_level: Optional[str] = None

    # Primary intelligence discipline (HUMINT, SIGINT, OSINT, GEOINT, MASINT …)
    specialization: Optional[str] = None

    # Analytical techniques the analyst is certified / trained in
    analytical_methods: List[str] = []

    # Current task or assignment
    current_assignment: Optional[str] = None

    # Number of finished reports produced (lifetime or current cycle)
    reports_produced: int = 0

    # Databases / systems the analyst has access to
    systems_access: List[str] = []

    # Languages spoken (useful for HUMINT/SIGINT analysis)
    languages: List[str] = []

    active: bool = True
    contact_email: Optional[str] = None
    contact_phone: Optional[str] = None
    notes: Optional[str] = None
