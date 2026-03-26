from typing import Optional
from sqlalchemy import Boolean, Integer, JSON, String
from sqlalchemy.orm import Mapped, mapped_column
from model.orm.base import Base


class IntelligenceOfficerOrm(Base):
    __tablename__ = "intelligence_officer"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    case_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True, index=True)
    name: Mapped[str] = mapped_column(String, default="")
    rank: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    designation: Mapped[str] = mapped_column(String(10), default="S2")
    unit: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    clearance_level: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    area_of_responsibility: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    subordinate_analysts: Mapped[int] = mapped_column(Integer, default=0)
    reporting_to: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    current_assessment: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    intelligence_priorities: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    intelligence_products: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    active: Mapped[bool] = mapped_column(Boolean, default=True)
    contact_email: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    contact_phone: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    notes: Mapped[Optional[str]] = mapped_column(String, nullable=True)
