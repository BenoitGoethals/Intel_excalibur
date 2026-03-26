from datetime import datetime
from typing import List
from uuid import uuid4
from pydantic import BaseModel, Field


class CounterInt(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    case_id: Optional[str] = None  # 0..1 link to IntelCase
    operation_name: str = ""
    operation_start_date: datetime = datetime.min
    operation_end_date: datetime = datetime.min
    targets: List[str] = []
    suspects: List[str] = []
    tactics_used: List[str] = []
    techniques_used: List[str] = []
    intelligence_sources: List[str] = []
    analysis: str = ""
    findings: str = ""
    countermeasures: List[str] = []
    recommendations: List[str] = []
