from typing import List, Optional
from uuid import uuid4
from fastapi import APIRouter, HTTPException
from api.pydantic_mode.social_media import SocialMedia

router = APIRouter(prefix="/social-media", tags=["Social Media"])
_db: dict[str, SocialMedia] = {}


@router.get("/", response_model=List[SocialMedia])
def list_all(
    platform: Optional[str] = None,
    username: Optional[str] = None,
    location: Optional[str] = None,
    private_account: Optional[bool] = None,
):
    items = list(_db.values())
    if platform:
        items = [i for i in items if i.platform and platform.lower() in i.platform.lower()]
    if username:
        items = [i for i in items if i.username and username.lower() in i.username.lower()]
    if location:
        items = [i for i in items if i.location and location.lower() in i.location.lower()]
    if private_account is not None:
        items = [i for i in items if i.private_account == private_account]
    return items


@router.get("/{id}", response_model=SocialMedia)
def get_one(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="SocialMedia not found")
    return _db[id]


@router.post("/", response_model=SocialMedia, status_code=201)
def create(item: SocialMedia):
    item.id = str(uuid4())
    _db[item.id] = item
    return item


@router.put("/{id}", response_model=SocialMedia)
def update(id: str, item: SocialMedia):
    if id not in _db:
        raise HTTPException(status_code=404, detail="SocialMedia not found")
    item.id = id
    _db[id] = item
    return item


@router.delete("/{id}", status_code=204)
def delete(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="SocialMedia not found")
    del _db[id]
