from datetime import datetime
from typing import List, Optional
from pydantic import Field
from model.base_intel import BaseIntel
from model.list_item import ListItemPhoto
from model.type_intel import TypeIntel


class PersonOfInterest(BaseIntel):
    intel_type: TypeIntel = TypeIntel.OTHER
    name: str = ""
    alias: str = ""
    date_of_birth: datetime = Field(default_factory=datetime.now)
    nationality: Optional[str] = "BE"
    height: str = ""
    weight: str = ""
    eye_color: str = ""
    hair_color: str = ""
    address: str = ""
    phone_number: str = ""
    email: str = ""
    affiliations: str = ""
    relationships: str = ""
    criminal_record: str = ""
    suspicious_activities: str = ""
    threat_level: int = 0
    notes: str = ""
    political_group: str = ""
    pictures: List[ListItemPhoto] = []
