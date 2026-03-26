from typing import Optional
from sqlalchemy import String, JSON, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from model.orm.base_intel_orm import BaseIntelOrm


class CybIntOrm(BaseIntelOrm):
    __tablename__ = "cyb_int"

    id: Mapped[str] = mapped_column(ForeignKey("base_intel.id"), primary_key=True)
    incident_type: Mapped[str] = mapped_column(String(50), default="EmailPhishing")
    incident_description: Mapped[str] = mapped_column(String, default="")
    attribution: Mapped[str] = mapped_column(String, default="")
    tt_ps: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    exploited_vulnerabilities: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    impact_assessment: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    mitigation_recommendations: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    timeline: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    indicators_of_compromise: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    malware_analysis: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    prevention_recommendations: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": "CyberInt",
    }
