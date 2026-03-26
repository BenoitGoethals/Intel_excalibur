"""
Counterintelligence (CI) Agent
Detects, identifies and neutralises threats such as espionage,
insider threats, sabotage and foreign intelligence activity.
"""
from typing import List, Optional
from uuid import uuid4
from pydantic import BaseModel, Field


class CIAgent(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    case_id: Optional[str] = None  # 0..1 link to IntelCase

    name: str = ""
    rank: Optional[str] = None
    unit: Optional[str] = None
    clearance_level: Optional[str] = None

    # CI discipline: espionage detection / insider threats / sabotage / TSCM / FIE
    ci_specialty: Optional[str] = None

    # Categories of threat this agent focuses on
    target_threats: List[str] = []

    # Number of CI investigations currently open
    active_investigations: int = 0

    # Alias / cover identity (handle with care)
    cover_identity: Optional[str] = None

    # Agencies or units this agent coordinates with
    partner_agencies: List[str] = []

    # Whether this agent is currently undercover
    undercover: bool = False

    active: bool = True
    contact_email: Optional[str] = None
    contact_phone: Optional[str] = None
    notes: Optional[str] = None
