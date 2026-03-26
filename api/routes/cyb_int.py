from typing import List, Optional
from uuid import uuid4
from fastapi import APIRouter, HTTPException
from api.pydantic_mode.cyb_int import CybInt

router = APIRouter(prefix="/cyb-int", tags=["CYBINT"])
_db: dict[str, CybInt] = {}


@router.get("/", response_model=List[CybInt])
def list_all(
    incident_type: Optional[str] = None,
    attribution: Optional[str] = None,
):
    items = list(_db.values())
    if incident_type:
        items = [i for i in items if i.incident_type.value == incident_type]
    if attribution:
        items = [i for i in items if attribution.lower() in i.attribution.lower()]
    return items


@router.get("/{id}", response_model=CybInt)
def get_one(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="CybInt not found")
    return _db[id]


@router.post("/", response_model=CybInt, status_code=201)
def create(item: CybInt):
    item.id = str(uuid4())
    _db[item.id] = item
    return item


@router.put("/{id}", response_model=CybInt)
def update(id: str, item: CybInt):
    if id not in _db:
        raise HTTPException(status_code=404, detail="CybInt not found")
    item.id = id
    _db[id] = item
    return item


@router.delete("/{id}", status_code=204)
def delete(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="CybInt not found")
    del _db[id]
