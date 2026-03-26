from datetime import datetime
from typing import List
from pydantic import BaseModel


class HumanSource(BaseModel):
    id: int = 0
    name: str = ""
    for_name: str = ""
    additional_info: List[str] = []
    dtg_injected: datetime = datetime.min
