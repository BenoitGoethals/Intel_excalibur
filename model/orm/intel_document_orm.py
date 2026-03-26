from datetime import datetime
from typing import Optional
from sqlalchemy import String, DateTime, JSON, LargeBinary, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from model.orm.base_intel_orm import BaseIntelOrm


class IntelDocumentOrm(BaseIntelOrm):
    __tablename__ = "intel_document"

    id: Mapped[str] = mapped_column(ForeignKey("base_intel.id"), primary_key=True)
    document_type: Mapped[str] = mapped_column(String(10), default="Nothing")
    description: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    long_description: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    file_name: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    content: Mapped[Optional[bytes]] = mapped_column(LargeBinary, nullable=True)
    time_created: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    keywords: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": "intel_document",
    }
