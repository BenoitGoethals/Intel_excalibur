from typing import List, Optional
from uuid import uuid4
from fastapi import APIRouter, HTTPException
from api.pydantic_mode.intelligence_officer import IntelligenceOfficer

router = APIRouter(prefix="/intelligence-officers", tags=["Intelligence Officers"])
_db: dict[str, IntelligenceOfficer] = {}


@router.get("/", response_model=List[IntelligenceOfficer])
def list_all(
    name: Optional[str] = None,
    designation: Optional[str] = None,
    unit: Optional[str] = None,
    active: Optional[bool] = None,
):
    items = list(_db.values())
    if name:
        items = [i for i in items if name.lower() in i.name.lower()]
    if designation:
        items = [i for i in items if i.designation == designation]
    if unit:
        items = [i for i in items if i.unit and unit.lower() in i.unit.lower()]
    if active is not None:
        items = [i for i in items if i.active == active]
    return items


@router.get("/{id}", response_model=IntelligenceOfficer)
def get_one(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="IntelligenceOfficer not found")
    return _db[id]


@router.post("/", response_model=IntelligenceOfficer, status_code=201)
def create(item: IntelligenceOfficer):
    item.id = str(uuid4())
    _db[item.id] = item
    return item


@router.put("/{id}", response_model=IntelligenceOfficer)
def update(id: str, item: IntelligenceOfficer):
    if id not in _db:
        raise HTTPException(status_code=404, detail="IntelligenceOfficer not found")
    item.id = id
    _db[id] = item
    return item


@router.delete("/{id}", status_code=204)
def delete(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="IntelligenceOfficer not found")
    del _db[id]
