from typing import List, Optional
from uuid import uuid4
from fastapi import APIRouter, HTTPException
from api.pydantic_mode.person_of_interest import PersonOfInterest

router = APIRouter(prefix="/persons-of-interest", tags=["Persons of Interest"])
_db: dict[str, PersonOfInterest] = {}


@router.get("/", response_model=List[PersonOfInterest])
def list_all(
    name: Optional[str] = None,
    alias: Optional[str] = None,
    nationality: Optional[str] = None,
    political_group: Optional[str] = None,
    min_threat_level: Optional[int] = None,
    max_threat_level: Optional[int] = None,
):
    items = list(_db.values())
    if name:
        items = [i for i in items if name.lower() in i.name.lower()]
    if alias:
        items = [i for i in items if alias.lower() in i.alias.lower()]
    if nationality:
        items = [i for i in items if i.nationality and nationality.lower() in i.nationality.lower()]
    if political_group:
        items = [i for i in items if political_group.lower() in i.political_group.lower()]
    if min_threat_level is not None:
        items = [i for i in items if i.threat_level >= min_threat_level]
    if max_threat_level is not None:
        items = [i for i in items if i.threat_level <= max_threat_level]
    return items


@router.get("/{id}", response_model=PersonOfInterest)
def get_one(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="PersonOfInterest not found")
    return _db[id]


@router.post("/", response_model=PersonOfInterest, status_code=201)
def create(item: PersonOfInterest):
    item.id = str(uuid4())
    _db[item.id] = item
    return item


@router.put("/{id}", response_model=PersonOfInterest)
def update(id: str, item: PersonOfInterest):
    if id not in _db:
        raise HTTPException(status_code=404, detail="PersonOfInterest not found")
    item.id = id
    _db[id] = item
    return item


@router.delete("/{id}", status_code=204)
def delete(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="PersonOfInterest not found")
    del _db[id]
