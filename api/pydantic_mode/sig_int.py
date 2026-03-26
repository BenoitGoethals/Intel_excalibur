from datetime import datetime
from typing import List
from uuid import uuid4
from pydantic import BaseModel, Field


class SigInt(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    case_id: Optional[str] = None  # 0..1 link to IntelCase
    signal_type: str = ""
    signal_frequency: str = ""
    signal_source: str = ""
    intercept_date_time: datetime = datetime.min
    sender: str = ""
    receiver: str = ""
    message_content: str = ""
    analysis: str = ""
    interpretation: str = ""
    sender_location: str = ""
    receiver_location: str = ""
    recommendations: List[str] = []
