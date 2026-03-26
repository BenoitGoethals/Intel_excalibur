from typing import List, Optional
from fastapi import APIRouter, HTTPException
from api.pydantic_mode.geo_int import GeoInt

router = APIRouter(prefix="/geo-int", tags=["GEOINT"])
_db: dict[str, GeoInt] = {}


@router.get("/", response_model=List[GeoInt])
def list_all(
    target_location: Optional[str] = None,
    weather_conditions: Optional[str] = None,
    natural_hazards: Optional[str] = None,
):
    items = list(_db.values())
    if target_location:
        items = [i for i in items if target_location.lower() in i.target_location.lower()]
    if weather_conditions:
        items = [i for i in items if weather_conditions.lower() in i.weather_conditions.lower()]
    if natural_hazards:
        items = [i for i in items if natural_hazards.lower() in i.natural_hazards.lower()]
    return items


@router.get("/{id}", response_model=GeoInt)
def get_one(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="GeoInt not found")
    return _db[id]


@router.post("/", response_model=GeoInt, status_code=201)
def create(item: GeoInt):
    _db[item.id] = item
    return item


@router.put("/{id}", response_model=GeoInt)
def update(id: str, item: GeoInt):
    if id not in _db:
        raise HTTPException(status_code=404, detail="GeoInt not found")
    item.id = id
    _db[id] = item
    return item


@router.delete("/{id}", status_code=204)
def delete(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="GeoInt not found")
    del _db[id]
