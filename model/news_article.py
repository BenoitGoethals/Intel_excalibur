from datetime import datetime
from typing import List, Optional
from model.base_intel import BaseIntel
from model.type_intel import TypeIntel


class NewsArticle(BaseIntel):
    intel_type: TypeIntel = TypeIntel.NEWS_ARTICLE
    title: Optional[str] = None
    url: Optional[str] = None
    author: Optional[str] = None
    published_date: Optional[datetime] = None
    content: Optional[str] = None
    source: Optional[str] = None
    keywords: List[str] = []
