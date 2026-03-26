from datetime import datetime
from typing import List, Optional
from api.pydantic_mode.base_intel import BaseIntel
from api.pydantic_mode.enums import InvestigationStatus
from api.pydantic_mode.intel_document import IntelDocument
from api.pydantic_mode.list_item import ListItem
from api.pydantic_mode.person_of_interest import PersonOfInterest


class IntelInvestigationFile(BaseIntel):
    case_number: Optional[str] = None
    started_date_time: Optional[datetime] = None
    ended_date_time: Optional[datetime] = None
    description: Optional[str] = None
    person_of_interests: List[PersonOfInterest] = []
    long_description: Optional[str] = None
    evidence_collected: List[BaseIntel] = []
    intel_documents: List[IntelDocument] = []
    investigator_name: Optional[str] = None
    investigator_badge_number: Optional[str] = None
    investigator_note: Optional[str] = None
    expert_opinions: List[ListItem] = []
    investigation_status: InvestigationStatus = InvestigationStatus.INIT
    conclusion: Optional[str] = None
