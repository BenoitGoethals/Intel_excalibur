from typing import Optional
from sqlalchemy import Boolean, Integer, JSON, String
from sqlalchemy.orm import Mapped, mapped_column
from model.orm.base import Base


class CIAgentOrm(Base):
    __tablename__ = "ci_agent"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    case_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True, index=True)
    name: Mapped[str] = mapped_column(String, default="")
    rank: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    unit: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    clearance_level: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    ci_specialty: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    target_threats: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    active_investigations: Mapped[int] = mapped_column(Integer, default=0)
    cover_identity: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    partner_agencies: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    undercover: Mapped[bool] = mapped_column(Boolean, default=False)
    active: Mapped[bool] = mapped_column(Boolean, default=True)
    contact_email: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    contact_phone: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    notes: Mapped[Optional[str]] = mapped_column(String, nullable=True)
