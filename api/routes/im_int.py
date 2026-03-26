from typing import List, Optional
from fastapi import APIRouter, HTTPException
from api.pydantic_mode.im_int import ImInt

router = APIRouter(prefix="/im-int", tags=["IMINT"])
_db: dict[str, ImInt] = {}


@router.get("/", response_model=List[ImInt])
def list_all(
    target_name: Optional[str] = None,
    target_location: Optional[str] = None,
    image_format: Optional[str] = None,
):
    items = list(_db.values())
    if target_name:
        items = [i for i in items if target_name.lower() in i.target_name.lower()]
    if target_location:
        items = [i for i in items if target_location.lower() in i.target_location.lower()]
    if image_format:
        items = [i for i in items if image_format.lower() in i.image_format.lower()]
    return items


@router.get("/{id}", response_model=ImInt)
def get_one(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="ImInt not found")
    return _db[id]


@router.post("/", response_model=ImInt, status_code=201)
def create(item: ImInt):
    _db[item.id] = item
    return item


@router.put("/{id}", response_model=ImInt)
def update(id: str, item: ImInt):
    if id not in _db:
        raise HTTPException(status_code=404, detail="ImInt not found")
    item.id = id
    _db[id] = item
    return item


@router.delete("/{id}", status_code=204)
def delete(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="ImInt not found")
    del _db[id]
