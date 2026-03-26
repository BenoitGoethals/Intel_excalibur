from datetime import datetime
from typing import List, Optional
from model.base_intel import BaseIntel
from model.list_item import ListItem
from model.type_intel import TypeIntel


class OpenSourceInt(BaseIntel):
    intel_type: TypeIntel = TypeIntel.OPEN_SOURCE
    source_name: Optional[str] = None
    source_type: Optional[str] = None
    source_url: Optional[str] = None
    target_name: Optional[str] = None
    target_location: Optional[str] = None
    report_date: Optional[datetime] = None
    gathered_information: List[ListItem] = []
    analysis: Optional[str] = None
    implications: Optional[str] = None
    recommendations: List[ListItem] = []
