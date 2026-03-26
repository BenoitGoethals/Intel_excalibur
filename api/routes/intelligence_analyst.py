from typing import List, Optional
from uuid import uuid4
from fastapi import APIRouter, HTTPException
from api.pydantic_mode.intelligence_analyst import IntelligenceAnalyst

router = APIRouter(prefix="/intelligence-analysts", tags=["Intelligence Analysts"])
_db: dict[str, IntelligenceAnalyst] = {}


@router.get("/", response_model=List[IntelligenceAnalyst])
def list_all(
    name: Optional[str] = None,
    specialization: Optional[str] = None,
    unit: Optional[str] = None,
    active: Optional[bool] = None,
):
    items = list(_db.values())
    if name:
        items = [i for i in items if name.lower() in i.name.lower()]
    if specialization:
        items = [i for i in items if i.specialization and specialization.lower() in i.specialization.lower()]
    if unit:
        items = [i for i in items if i.unit and unit.lower() in i.unit.lower()]
    if active is not None:
        items = [i for i in items if i.active == active]
    return items


@router.get("/{id}", response_model=IntelligenceAnalyst)
def get_one(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="IntelligenceAnalyst not found")
    return _db[id]


@router.post("/", response_model=IntelligenceAnalyst, status_code=201)
def create(item: IntelligenceAnalyst):
    item.id = str(uuid4())
    _db[item.id] = item
    return item


@router.put("/{id}", response_model=IntelligenceAnalyst)
def update(id: str, item: IntelligenceAnalyst):
    if id not in _db:
        raise HTTPException(status_code=404, detail="IntelligenceAnalyst not found")
    item.id = id
    _db[id] = item
    return item


@router.delete("/{id}", status_code=204)
def delete(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="IntelligenceAnalyst not found")
    del _db[id]
