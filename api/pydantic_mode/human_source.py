from datetime import datetime
from typing import List
from pydantic import BaseModel


class HumanSource(BaseModel):
    id: int = 0
    case_id: Optional[str] = None  # 0..1 link to IntelCase
    name: str = ""
    for_name: str = ""
    additional_info: List[str] = []
    dtg_injected: datetime = datetime.min

    def __str__(self) -> str:
        return f"Name: {self.name}, ForName: {self.for_name}"
