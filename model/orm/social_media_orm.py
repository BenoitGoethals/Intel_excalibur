from datetime import datetime
from typing import Optional
from sqlalchemy import String, Integer, Boolean, DateTime, JSON, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from model.orm.base_intel_orm import BaseIntelOrm


class SocialMediaOrm(BaseIntelOrm):
    __tablename__ = "social_media"

    id: Mapped[str] = mapped_column(ForeignKey("base_intel.id"), primary_key=True)
    username: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    display_name: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    bio: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    account_creation_date: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    platform: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    followers_count: Mapped[int] = mapped_column(Integer, default=0)
    following_count: Mapped[int] = mapped_column(Integer, default=0)
    post_count: Mapped[int] = mapped_column(Integer, default=0)
    recent_posts: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    engagement_rate: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    sentiment_analysis: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    location: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    private_account: Mapped[bool] = mapped_column(Boolean, default=False)
    two_factor_authentication: Mapped[bool] = mapped_column(Boolean, default=False)

    __mapper_args__ = {
        "polymorphic_identity": "SocialMedia",
    }
