from datetime import datetime
from typing import Optional
from sqlalchemy import String, Integer, DateTime, JSON, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from model.orm.base_intel_orm import BaseIntelOrm


class PersonOfInterestOrm(BaseIntelOrm):
    __tablename__ = "person_of_interest"

    id: Mapped[str] = mapped_column(ForeignKey("base_intel.id"), primary_key=True)
    name: Mapped[str] = mapped_column(String, default="")
    alias: Mapped[str] = mapped_column(String, default="")
    date_of_birth: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    nationality: Mapped[Optional[str]] = mapped_column(String, nullable=True, default="BE")
    height: Mapped[str] = mapped_column(String, default="")
    weight: Mapped[str] = mapped_column(String, default="")
    eye_color: Mapped[str] = mapped_column(String, default="")
    hair_color: Mapped[str] = mapped_column(String, default="")
    address: Mapped[str] = mapped_column(String, default="")
    phone_number: Mapped[str] = mapped_column(String, default="")
    email: Mapped[str] = mapped_column(String, default="")
    affiliations: Mapped[str] = mapped_column(String, default="")
    relationships: Mapped[str] = mapped_column(String, default="")
    criminal_record: Mapped[str] = mapped_column(String, default="")
    suspicious_activities: Mapped[str] = mapped_column(String, default="")
    threat_level: Mapped[int] = mapped_column(Integer, default=0)
    notes: Mapped[str] = mapped_column(String, default="")
    political_group: Mapped[str] = mapped_column(String, default="")
    pictures: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": "person_of_interest",
    }
