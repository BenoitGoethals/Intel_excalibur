from datetime import datetime
from decimal import Decimal
from typing import List
from pydantic import BaseModel


class FinancialInt(BaseModel):
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
