from datetime import datetime
from typing import Optional
from sqlalchemy import String, DateTime, JSON, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from model.orm.base_intel_orm import BaseIntelOrm


class GeneralIntelOrm(BaseIntelOrm):
    __tablename__ = "general_intel"

    id: Mapped[str] = mapped_column(ForeignKey("base_intel.id"), primary_key=True)
    name: Mapped[str] = mapped_column(String, default="")
    dtg_injected: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    dtg_occurrence: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    human_source: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    additional_info: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    report_title: Mapped[str] = mapped_column(String, default="")
    report_date: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    reporting_agency: Mapped[str] = mapped_column(String, default="")
    incident_location: Mapped[str] = mapped_column(String, default="")
    incident_date_time: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    key_players: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    intelligence_sources: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    analysis: Mapped[str] = mapped_column(String, default="")
    findings: Mapped[str] = mapped_column(String, default="")
    recommendations: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": "general_intel",
    }
