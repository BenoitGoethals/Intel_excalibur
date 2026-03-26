from typing import Optional
from pydantic import BaseModel


class OperatorIntel(BaseModel):
    id: int = 0
    name: Optional[str] = None
    for_name: Optional[str] = None
    serial_nbr: Optional[str] = None
