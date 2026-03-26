from datetime import datetime
from typing import Optional
from sqlalchemy import Boolean, DateTime, Integer, JSON, String
from sqlalchemy.orm import Mapped, mapped_column
from model.orm.base import Base


class IntelligenceCollectorOrm(Base):
    __tablename__ = "intelligence_collector"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    case_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True, index=True)
    name: Mapped[str] = mapped_column(String, default="")
    rank: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    unit: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    clearance_level: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    collection_method: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    target_area: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    collection_assets: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    active_operations: Mapped[int] = mapped_column(Integer, default=0)
    last_collection_date: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    qualifications: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    languages: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    active: Mapped[bool] = mapped_column(Boolean, default=True)
    contact_email: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    contact_phone: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    notes: Mapped[Optional[str]] = mapped_column(String, nullable=True)
