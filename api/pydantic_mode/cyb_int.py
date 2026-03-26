from typing import List, Optional
from api.pydantic_mode.base_intel import BaseIntel
from api.pydantic_mode.enums import TypeOfCybInt
from api.pydantic_mode.list_item import ListItem, ListItemDate
from api.pydantic_mode.type_intel import TypeIntel


class CybInt(BaseIntel):
    intel_type: TypeIntel = TypeIntel.CYBER_INT
    incident_type: TypeOfCybInt = TypeOfCybInt.EMAIL_PHISHING
    incident_description: str = ""
    attribution: str = ""
    tt_ps: List[ListItem] = []
    exploited_vulnerabilities: List[ListItem] = []
    impact_assessment: Optional[str] = "Test"
    mitigation_recommendations: List[ListItem] = []
    timeline: List[ListItemDate] = []
    indicators_of_compromise: List[ListItem] = []
    malware_analysis: Optional[str] = "test"
    prevention_recommendations: List[ListItem] = []
