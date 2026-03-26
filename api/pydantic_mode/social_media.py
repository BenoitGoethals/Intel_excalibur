from datetime import datetime
from typing import List, Optional
from pydantic import Field
from api.pydantic_mode.base_intel import BaseIntel
from api.pydantic_mode.list_item import ListItem
from api.pydantic_mode.type_intel import TypeIntel


class SocialMedia(BaseIntel):
    intel_type: TypeIntel = TypeIntel.SOCIAL_MEDIA
    username: Optional[str] = None
    display_name: Optional[str] = None
    bio: Optional[str] = None
    account_creation_date: Optional[datetime] = Field(default_factory=datetime.now)
    platform: Optional[str] = None
    followers_count: int = 0
    following_count: int = 0
    post_count: int = 0
    recent_posts: List[ListItem] = []
    engagement_rate: Optional[str] = None
    sentiment_analysis: Optional[str] = None
    location: Optional[str] = None
    private_account: bool = False
    two_factor_authentication: bool = False
