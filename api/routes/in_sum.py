from typing import List, Optional
from uuid import uuid4
from fastapi import APIRouter, HTTPException
from api.pydantic_mode.in_sum import InSum

router = APIRouter(prefix="/in-sum", tags=["Intelligence Summary"])
_db: dict[str, InSum] = {}


@router.get("/", response_model=List[InSum])
def list_all(
    name: Optional[str] = None,
    reporting_agency: Optional[str] = None,
    incident_location: Optional[str] = None,
    short_description: Optional[str] = None,
):
    items = list(_db.values())
    if name:
        items = [i for i in items if name.lower() in i.name.lower()]
    if reporting_agency:
        items = [i for i in items if reporting_agency.lower() in i.reporting_agency.lower()]
    if incident_location:
        items = [i for i in items if incident_location.lower() in i.incident_location.lower()]
    if short_description:
        items = [i for i in items if short_description.lower() in i.short_description.lower()]
    return items


@router.get("/{id}", response_model=InSum)
def get_one(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="InSum not found")
    return _db[id]


@router.post("/", response_model=InSum, status_code=201)
def create(item: InSum):
    item.id = str(uuid4())
    _db[item.id] = item
    return item


@router.put("/{id}", response_model=InSum)
def update(id: str, item: InSum):
    if id not in _db:
        raise HTTPException(status_code=404, detail="InSum not found")
    item.id = id
    _db[id] = item
    return item


@router.delete("/{id}", status_code=204)
def delete(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="InSum not found")
    del _db[id]
