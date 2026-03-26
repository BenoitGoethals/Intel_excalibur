from datetime import datetime
from typing import Optional
from pydantic import Field
from model.base_intel import BaseIntel
from model.enums import Gender
from model.type_intel import TypeIntel


class Informant(BaseIntel):
    intel_type: TypeIntel = TypeIntel.INFORMANT
    informant_name: Optional[str] = None
    informant_code_name: Optional[str] = None
    age: Optional[int] = 20
    gender: Gender = Gender.MALE
    contact_number: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    informant_role: Optional[str] = None
    background_info: Optional[str] = None
    reliability_rating: Optional[int] = 1
    intel_provided: Optional[str] = None
    areas_of_expertise: Optional[str] = None
    active_status: Optional[bool] = None
    last_contact_date: Optional[datetime] = Field(default_factory=datetime.now)
