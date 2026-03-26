from datetime import datetime
from decimal import Decimal
from typing import List
from uuid import uuid4
from pydantic import BaseModel, Field


class FinancialInt(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    case_id: Optional[str] = None  # 0..1 link to IntelCase
    transaction_type: str = ""
    amount: Decimal = Decimal("0.0")
    transaction_date: datetime = datetime.min
    counterparty: str = ""
    involved_parties: List[str] = []
    suspicious_activity_description: str = ""
    regulatory_compliance_status: str = ""
    investigating_agency: str = ""
    investigation_start_date: datetime = datetime.min
    investigation_status: str = ""
    investigation_findings: str = ""
    recommendations: List[str] = []
