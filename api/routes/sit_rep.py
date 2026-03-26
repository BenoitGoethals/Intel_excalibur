from typing import List, Optional
from fastapi import APIRouter, HTTPException
from api.pydantic_mode.sit_rep import SitRep

router = APIRouter(prefix="/sit-rep", tags=["SITREP"])
_db: dict[str, SitRep] = {}


@router.get("/", response_model=List[SitRep])
def list_all(
    reporting_unit: Optional[str] = None,
    location: Optional[str] = None,
    weather_conditions: Optional[str] = None,
):
    items = list(_db.values())
    if reporting_unit:
        items = [i for i in items if reporting_unit.lower() in i.reporting_unit.lower()]
    if location:
        items = [i for i in items if location.lower() in i.location.lower()]
    if weather_conditions:
        items = [i for i in items if weather_conditions.lower() in i.weather_conditions.lower()]
    return items


@router.get("/{id}", response_model=SitRep)
def get_one(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="SitRep not found")
    return _db[id]


@router.post("/", response_model=SitRep, status_code=201)
def create(item: SitRep):
    _db[item.id] = item
    return item


@router.put("/{id}", response_model=SitRep)
def update(id: str, item: SitRep):
    if id not in _db:
        raise HTTPException(status_code=404, detail="SitRep not found")
    item.id = id
    _db[id] = item
    return item


@router.delete("/{id}", status_code=204)
def delete(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="SitRep not found")
    del _db[id]
