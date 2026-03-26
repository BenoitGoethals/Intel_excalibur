from datetime import datetime
from typing import List, Optional
from pydantic import Field
from api.pydantic_mode.base_intel import BaseIntel
from api.pydantic_mode.enums import HumIntType
from api.pydantic_mode.list_item import ListItem
from api.pydantic_mode.type_intel import TypeIntel


class HumInt(BaseIntel):
    intel_type: TypeIntel = TypeIntel.HUMINT
    source_information: str = ""
    hum_int_type: HumIntType = HumIntType.ADVISORS
    context_background: str = ""
    time_location: str = ""
    reliability_credibility: str = ""
    accuracy_of_details: str = ""
    assessment_and_analysis: str = ""
    classification_handling_instructions: str = ""
    source_name: str = ""
    source_type: str = ""
    source_affiliation: str = ""
    reliability_rating: int = 0
    access_level: str = ""
    contact_name: str = ""
    contact_title: str = ""
    contact_phone_number: str = ""
    contact_email: str = ""
    intelligence_details: List[ListItem] = []
    operational_status: str = ""
    last_contact_date: Optional[datetime] = Field(default_factory=datetime.now)
