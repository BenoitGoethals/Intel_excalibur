from typing import List, Optional
from uuid import uuid4
from fastapi import APIRouter, HTTPException
from api.pydantic_mode.intelligence_collector import IntelligenceCollector

router = APIRouter(prefix="/intelligence-collectors", tags=["Intelligence Collectors"])
_db: dict[str, IntelligenceCollector] = {}


@router.get("/", response_model=List[IntelligenceCollector])
def list_all(
    name: Optional[str] = None,
    collection_method: Optional[str] = None,
    unit: Optional[str] = None,
    active: Optional[bool] = None,
):
    items = list(_db.values())
    if name:
        items = [i for i in items if name.lower() in i.name.lower()]
    if collection_method:
        items = [i for i in items if i.collection_method and collection_method.lower() in i.collection_method.lower()]
    if unit:
        items = [i for i in items if i.unit and unit.lower() in i.unit.lower()]
    if active is not None:
        items = [i for i in items if i.active == active]
    return items


@router.get("/{id}", response_model=IntelligenceCollector)
def get_one(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="IntelligenceCollector not found")
    return _db[id]


@router.post("/", response_model=IntelligenceCollector, status_code=201)
def create(item: IntelligenceCollector):
    item.id = str(uuid4())
    _db[item.id] = item
    return item


@router.put("/{id}", response_model=IntelligenceCollector)
def update(id: str, item: IntelligenceCollector):
    if id not in _db:
        raise HTTPException(status_code=404, detail="IntelligenceCollector not found")
    item.id = id
    _db[id] = item
    return item


@router.delete("/{id}", status_code=204)
def delete(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="IntelligenceCollector not found")
    del _db[id]
