from datetime import datetime
from typing import List, Optional
from pydantic import Field
from api.pydantic_mode.base_intel import BaseIntel
from api.pydantic_mode.human_source import HumanSource
from api.pydantic_mode.list_item import ListItem
from api.pydantic_mode.type_intel import TypeIntel


class GeneralIntel(BaseIntel):
    intel_type: TypeIntel = TypeIntel.OTHER
    name: str = ""
    dtg_injected: Optional[datetime] = None
    dtg_occurrence: Optional[datetime] = None
    human_source: HumanSource = Field(default_factory=HumanSource)
    additional_info: List[ListItem] = []
    report_title: str = ""
    report_date: Optional[datetime] = None
    reporting_agency: str = ""
    incident_location: str = ""
    incident_date_time: Optional[datetime] = None
    key_players: List[ListItem] = []
    intelligence_sources: List[ListItem] = []
    analysis: str = ""
    findings: str = ""
    recommendations: List[ListItem] = []
