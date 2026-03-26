from datetime import datetime
from typing import List
from pydantic import BaseModel


class CounterInt(BaseModel):
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
