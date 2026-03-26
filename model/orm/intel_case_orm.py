from datetime import datetime
from typing import Optional
from sqlalchemy import DateTime, JSON, String
from sqlalchemy.orm import Mapped, mapped_column
from model.orm.base import Base


class IntelCaseOrm(Base):
    __tablename__ = "intel_case"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)

    # Identity
    case_number: Mapped[str] = mapped_column(String(50), default="", index=True)
    title: Mapped[str] = mapped_column(String, default="")

    # Classification & priority
    classification: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    priority: Mapped[str] = mapped_column(String(20), default="Medium")
    status: Mapped[str] = mapped_column(String(20), default="Draft", index=True)

    # Dates
    start_date: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    end_date: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    # People
    case_officer_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True, index=True)
    case_officer_name: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    ci_agent_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True, index=True)
    ci_agent_name: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    assigned_analyst_ids: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    persons_of_interest_ids: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)

    # Narrative
    description: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    objective: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    area_of_interest: Mapped[Optional[str]] = mapped_column(String, nullable=True)

    # Linked intel — list of {intel_type, intel_id, title}
    linked_intel: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    document_ids: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)

    # Outcome
    conclusions: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    recommendations: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    lessons_learned: Mapped[Optional[str]] = mapped_column(String, nullable=True)

    # Meta
    tags: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    notes: Mapped[Optional[str]] = mapped_column(String, nullable=True)
