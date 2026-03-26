from datetime import datetime
from typing import Optional
from sqlalchemy import String, DateTime, JSON, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from model.orm.base_intel_orm import BaseIntelOrm


class IntelInvestigationFileOrm(BaseIntelOrm):
    __tablename__ = "intel_investigation_file"

    id: Mapped[str] = mapped_column(ForeignKey("base_intel.id"), primary_key=True)
    case_number: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    started_date_time: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    ended_date_time: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    description: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    person_of_interests: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    long_description: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    evidence_collected: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    intel_documents: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    investigator_name: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    investigator_badge_number: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    investigator_note: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    expert_opinions: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    investigation_status: Mapped[str] = mapped_column(String(20), default="Init")
    conclusion: Mapped[Optional[str]] = mapped_column(String, nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": "intel_investigation_file",
    }
