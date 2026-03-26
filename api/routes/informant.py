from typing import List, Optional
from uuid import uuid4
from fastapi import APIRouter, HTTPException
from api.pydantic_mode.informant import Informant

router = APIRouter(prefix="/informants", tags=["Informants"])
_db: dict[str, Informant] = {}


@router.get("/", response_model=List[Informant])
def list_all(
    informant_role: Optional[str] = None,
    gender: Optional[str] = None,
    active_status: Optional[bool] = None,
    areas_of_expertise: Optional[str] = None,
    min_reliability: Optional[int] = None,
):
    items = list(_db.values())
    if informant_role:
        items = [i for i in items if i.informant_role and informant_role.lower() in i.informant_role.lower()]
    if gender:
        items = [i for i in items if i.gender.value == gender]
    if active_status is not None:
        items = [i for i in items if i.active_status == active_status]
    if areas_of_expertise:
        items = [i for i in items if i.areas_of_expertise and areas_of_expertise.lower() in i.areas_of_expertise.lower()]
    if min_reliability is not None:
        items = [i for i in items if i.reliability_rating is not None and i.reliability_rating >= min_reliability]
    return items


@router.get("/{id}", response_model=Informant)
def get_one(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="Informant not found")
    return _db[id]


@router.post("/", response_model=Informant, status_code=201)
def create(item: Informant):
    item.id = str(uuid4())
    _db[item.id] = item
    return item


@router.put("/{id}", response_model=Informant)
def update(id: str, item: Informant):
    if id not in _db:
        raise HTTPException(status_code=404, detail="Informant not found")
    item.id = id
    _db[id] = item
    return item


@router.delete("/{id}", status_code=204)
def delete(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="Informant not found")
    del _db[id]
