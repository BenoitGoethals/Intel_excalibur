from typing import Optional
from pydantic import BaseModel
from api.pydantic_mode.type_intel import TypeIntel


class BaseIntel(BaseModel):
    id: Optional[str] = None  # MongoDB _id
    intel_type: TypeIntel = TypeIntel.OTHER
    short_content: Optional[str] = None
    case_id: Optional[str] = None  # 0..1 link to IntelCase
