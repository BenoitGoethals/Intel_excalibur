"""
Intel Case — the central "case file" that ties together all intelligence,
people, documents and assigned roles into one investigation.

Linked intel is stored as a list of references so items from any intel
collection (HumInt, CybInt, NewsArticle …) can be attached without
tight foreign-key coupling:

    linked_intel: [
        {"intel_type": "HumInt",      "intel_id": "<uuid>", "title": "..."},
        {"intel_type": "NewsArticle", "intel_id": "<uuid>", "title": "..."},
    ]
"""
from datetime import datetime
from typing import Any, Dict, List, Optional
from uuid import uuid4
from pydantic import BaseModel, Field
from api.pydantic_mode.enums import IntelCasePriority, IntelCaseStatus


class LinkedIntel(BaseModel):
    """A lightweight reference to an intel item from any collection."""
    intel_type: str          # e.g. "HumInt", "CybInt", "NewsArticle"
    intel_id: str            # UUID of the record in its own table
    title: Optional[str] = None  # human-readable label for display


class IntelCase(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))

    # ── Identity ──────────────────────────────────────────────────────────
    case_number: str = ""        # e.g. "IC-2025-0042"
    title: str = ""

    # ── Classification & priority ─────────────────────────────────────────
    classification: Optional[str] = None          # UNCLASSIFIED / SECRET / …
    priority: IntelCasePriority = IntelCasePriority.MEDIUM
    status: IntelCaseStatus = IntelCaseStatus.DRAFT

    # ── Dates ─────────────────────────────────────────────────────────────
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    created_at: datetime = Field(default_factory=datetime.now)

    # ── People ────────────────────────────────────────────────────────────
    # Intelligence Officer responsible for this case
    case_officer_id: Optional[str] = None
    case_officer_name: Optional[str] = None   # denormalised for display

    # CI Agent assigned to this case
    ci_agent_id: Optional[str] = None
    ci_agent_name: Optional[str] = None       # denormalised for display

    # IDs of IntelligenceAnalyst records assigned to this case
    assigned_analyst_ids: List[str] = []

    # IDs of PersonOfInterest linked to this case
    persons_of_interest_ids: List[str] = []

    # ── Narrative ─────────────────────────────────────────────────────────
    description: Optional[str] = None
    objective: Optional[str] = None
    area_of_interest: Optional[str] = None

    # ── Intelligence items ────────────────────────────────────────────────
    # References to any intel record across all collections
    linked_intel: List[LinkedIntel] = []

    # IDs of IntelDocument records attached as evidence
    document_ids: List[str] = []

    # ── Outcome ───────────────────────────────────────────────────────────
    conclusions: Optional[str] = None
    recommendations: Optional[str] = None
    lessons_learned: Optional[str] = None

    # ── Meta ──────────────────────────────────────────────────────────────
    tags: List[str] = []
    notes: Optional[str] = None
