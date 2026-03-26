from datetime import datetime
from typing import Optional
from sqlalchemy import String, Integer, DateTime, JSON, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from model.orm.base_intel_orm import BaseIntelOrm


class HumIntOrm(BaseIntelOrm):
    __tablename__ = "hum_int"

    id: Mapped[str] = mapped_column(ForeignKey("base_intel.id"), primary_key=True)
    source_information: Mapped[str] = mapped_column(String, default="")
    hum_int_type: Mapped[str] = mapped_column(String(50), default="Advisors")
    context_background: Mapped[str] = mapped_column(String, default="")
    time_location: Mapped[str] = mapped_column(String, default="")
    reliability_credibility: Mapped[str] = mapped_column(String, default="")
    accuracy_of_details: Mapped[str] = mapped_column(String, default="")
    assessment_and_analysis: Mapped[str] = mapped_column(String, default="")
    classification_handling_instructions: Mapped[str] = mapped_column(String, default="")
    source_name: Mapped[str] = mapped_column(String, default="")
    source_type: Mapped[str] = mapped_column(String, default="")
    source_affiliation: Mapped[str] = mapped_column(String, default="")
    reliability_rating: Mapped[int] = mapped_column(Integer, default=0)
    access_level: Mapped[str] = mapped_column(String, default="")
    contact_name: Mapped[str] = mapped_column(String, default="")
    contact_title: Mapped[str] = mapped_column(String, default="")
    contact_phone_number: Mapped[str] = mapped_column(String, default="")
    contact_email: Mapped[str] = mapped_column(String, default="")
    intelligence_details: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    operational_status: Mapped[str] = mapped_column(String, default="")
    last_contact_date: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": "Humint",
    }
