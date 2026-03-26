from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ListItem(BaseModel):
    id: int = 0
    text: Optional[str] = None


class ListItemDate(BaseModel):
    id: int = 0
    dtg: Optional[datetime] = None


class ListItemPhoto(BaseModel):
    id: Optional[str] = None
    file_name: Optional[str] = None
    text: Optional[str] = None
    picture: Optional[bytes] = None
