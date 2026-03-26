from datetime import datetime
from typing import Optional
from sqlalchemy import String, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from model.orm.base_intel_orm import BaseIntelOrm


class InformantOrm(BaseIntelOrm):
    __tablename__ = "informant"

    id: Mapped[str] = mapped_column(ForeignKey("base_intel.id"), primary_key=True)
    informant_name: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    informant_code_name: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    age: Mapped[Optional[int]] = mapped_column(Integer, nullable=True, default=20)
    gender: Mapped[str] = mapped_column(String(10), default="Male")
    contact_number: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    email: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    address: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    informant_role: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    background_info: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    reliability_rating: Mapped[Optional[int]] = mapped_column(Integer, nullable=True, default=1)
    intel_provided: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    areas_of_expertise: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    active_status: Mapped[Optional[bool]] = mapped_column(Boolean, nullable=True)
    last_contact_date: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": "Informant",
    }
