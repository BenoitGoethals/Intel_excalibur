from typing import Optional
from pydantic import BaseModel
from model.type_intel import TypeIntel


class BaseIntel(BaseModel):
    id: Optional[str] = None
    intel_type: TypeIntel = TypeIntel.OTHER
    short_content: Optional[str] = None
