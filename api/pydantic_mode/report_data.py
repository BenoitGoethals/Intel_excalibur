from typing import Optional
from pydantic import BaseModel
from api.pydantic_mode.type_intel import TypeIntel


class ReportData(BaseModel):
    id: int = 0
    case_id: Optional[str] = None  # 0..1 link to IntelCase
    type_base_line: TypeIntel = TypeIntel.OTHER
    count: int = 0
    description: Optional[str] = None
