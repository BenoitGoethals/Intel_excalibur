from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from model.orm.base import Base


class BaseIntelOrm(Base):
    __tablename__ = "base_intel"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    intel_type: Mapped[str] = mapped_column(String(50), nullable=False)
    short_content: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    case_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True, index=True)

    __mapper_args__ = {
        "polymorphic_on": "intel_type",
        "polymorphic_identity": "base_intel",
    }
