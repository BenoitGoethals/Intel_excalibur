from datetime import datetime
from typing import List, Optional
from api.pydantic_mode.base_intel import BaseIntel
from api.pydantic_mode.enums import DocumentType


class IntelDocument(BaseIntel):
    document_type: DocumentType = DocumentType.NOTHING
    description: Optional[str] = None
    long_description: Optional[str] = None
    file_name: Optional[str] = None
    content: Optional[bytes] = None
    time_created: Optional[datetime] = None
    keywords: List[str] = []
