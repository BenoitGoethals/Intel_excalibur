from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from model.general_intel import GeneralIntel
from model.operator_intel import OperatorIntel


class Intel(BaseModel):
    id: int = 0
    short_description: str
    name: str
    dtg_injected: datetime
    long_description: Optional[str] = None
    operator_intel: Optional[OperatorIntel] = None
    _intel_reports: List[GeneralIntel] = []

    def add(self, intel_asset: GeneralIntel) -> None:
        self._intel_reports.append(intel_asset)

    def remove(self, intel_asset: GeneralIntel) -> None:
        self._intel_reports.remove(intel_asset)

    def clear(self) -> None:
        self._intel_reports.clear()

    def contains(self, intel_asset: GeneralIntel) -> bool:
        return intel_asset in self._intel_reports
