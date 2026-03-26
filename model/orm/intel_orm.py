from datetime import datetime
from typing import Optional
from sqlalchemy import String, Integer, DateTime, JSON
from sqlalchemy.orm import Mapped, mapped_column
from model.orm.base import Base


class IntelOrm(Base):
    __tablename__ = "intel"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    short_description: Mapped[str] = mapped_column(String, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    dtg_injected: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    long_description: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    operator_intel: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    intel_reports: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
