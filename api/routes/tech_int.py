from typing import List, Optional
from fastapi import APIRouter, HTTPException
from api.pydantic_mode.tech_int import TechInt

router = APIRouter(prefix="/tech-int", tags=["TECHINT"])
_db: dict[str, TechInt] = {}


@router.get("/", response_model=List[TechInt])
def list_all(
    technology_name: Optional[str] = None,
    manufacturer: Optional[str] = None,
    acquisition_source: Optional[str] = None,
):
    items = list(_db.values())
    if technology_name:
        items = [i for i in items if technology_name.lower() in i.technology_name.lower()]
    if manufacturer:
        items = [i for i in items if manufacturer.lower() in i.manufacturer.lower()]
    if acquisition_source:
        items = [i for i in items if acquisition_source.lower() in i.acquisition_source.lower()]
    return items


@router.get("/{id}", response_model=TechInt)
def get_one(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="TechInt not found")
    return _db[id]


@router.post("/", response_model=TechInt, status_code=201)
def create(item: TechInt):
    _db[item.id] = item
    return item


@router.put("/{id}", response_model=TechInt)
def update(id: str, item: TechInt):
    if id not in _db:
        raise HTTPException(status_code=404, detail="TechInt not found")
    item.id = id
    _db[id] = item
    return item


@router.delete("/{id}", status_code=204)
def delete(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="TechInt not found")
    del _db[id]
