from datetime import datetime
from typing import List, Optional
from model.base_intel import BaseIntel
from model.enums import InvestigationStatus
from model.intel_document import IntelDocument
from model.list_item import ListItem
from model.person_of_interest import PersonOfInterest


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
