from typing import Optional
from pydantic import BaseModel
from model.type_intel import TypeIntel


class ReportData(BaseModel):
    id: int = 0
    type_base_line: TypeIntel = TypeIntel.OTHER
    count: int = 0
    description: Optional[str] = None
