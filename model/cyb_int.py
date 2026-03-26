from typing import List, Optional
from model.base_intel import BaseIntel
from model.enums import TypeOfCybInt
from model.list_item import ListItem, ListItemDate
from model.type_intel import TypeIntel


class CybInt(BaseIntel):
    intel_type: TypeIntel = TypeIntel.CYBER_INT
    incident_type: TypeOfCybInt = TypeOfCybInt.EMAIL_PHISHING
    incident_description: str = ""
    attribution: str = ""
    tt_ps: List[ListItem] = []
    exploited_vulnerabilities: List[ListItem] = []
    impact_assessment: Optional[str] = None
    mitigation_recommendations: List[ListItem] = []
    timeline: List[ListItemDate] = []
    indicators_of_compromise: List[ListItem] = []
    malware_analysis: Optional[str] = None
    prevention_recommendations: List[ListItem] = []
