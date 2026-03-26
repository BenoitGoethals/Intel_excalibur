from typing import List, Optional
from uuid import uuid4
from fastapi import APIRouter, HTTPException
from api.pydantic_mode.open_source_int import OpenSourceInt

router = APIRouter(prefix="/open-source-int", tags=["OSINT"])
_db: dict[str, OpenSourceInt] = {}


@router.get("/", response_model=List[OpenSourceInt])
def list_all(
    source_name: Optional[str] = None,
    source_type: Optional[str] = None,
    target_name: Optional[str] = None,
    target_location: Optional[str] = None,
):
    items = list(_db.values())
    if source_name:
        items = [i for i in items if i.source_name and source_name.lower() in i.source_name.lower()]
    if source_type:
        items = [i for i in items if i.source_type and source_type.lower() in i.source_type.lower()]
    if target_name:
        items = [i for i in items if i.target_name and target_name.lower() in i.target_name.lower()]
    if target_location:
        items = [i for i in items if i.target_location and target_location.lower() in i.target_location.lower()]
    return items


@router.get("/{id}", response_model=OpenSourceInt)
def get_one(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="OpenSourceInt not found")
    return _db[id]


@router.post("/", response_model=OpenSourceInt, status_code=201)
def create(item: OpenSourceInt):
    item.id = str(uuid4())
    _db[item.id] = item
    return item


@router.put("/{id}", response_model=OpenSourceInt)
def update(id: str, item: OpenSourceInt):
    if id not in _db:
        raise HTTPException(status_code=404, detail="OpenSourceInt not found")
    item.id = id
    _db[id] = item
    return item


@router.delete("/{id}", status_code=204)
def delete(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="OpenSourceInt not found")
    del _db[id]
