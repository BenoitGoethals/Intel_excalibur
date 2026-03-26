from datetime import datetime
from typing import List
from pydantic import BaseModel


class SigInt(BaseModel):
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
