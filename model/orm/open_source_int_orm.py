from datetime import datetime
from typing import Optional
from sqlalchemy import String, DateTime, JSON, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from model.orm.base_intel_orm import BaseIntelOrm


class OpenSourceIntOrm(BaseIntelOrm):
    __tablename__ = "open_source_int"

    id: Mapped[str] = mapped_column(ForeignKey("base_intel.id"), primary_key=True)
    source_name: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    source_type: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    source_url: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    target_name: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    target_location: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    report_date: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    gathered_information: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    analysis: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    implications: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    recommendations: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": "OpenSource",
    }
