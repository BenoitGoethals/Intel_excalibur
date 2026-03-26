from typing import List, Optional
from uuid import uuid4
from fastapi import APIRouter, HTTPException
from api.pydantic_mode.general_intel import GeneralIntel

router = APIRouter(prefix="/general-intel", tags=["General Intel"])
_db: dict[str, GeneralIntel] = {}


@router.get("/", response_model=List[GeneralIntel])
def list_all(
    name: Optional[str] = None,
    reporting_agency: Optional[str] = None,
    incident_location: Optional[str] = None,
    intel_type: Optional[str] = None,
):
    items = list(_db.values())
    if name:
        items = [i for i in items if name.lower() in i.name.lower()]
    if reporting_agency:
        items = [i for i in items if reporting_agency.lower() in i.reporting_agency.lower()]
    if incident_location:
        items = [i for i in items if incident_location.lower() in i.incident_location.lower()]
    if intel_type:
        items = [i for i in items if i.intel_type.value == intel_type]
    return items


@router.get("/{id}", response_model=GeneralIntel)
def get_one(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="GeneralIntel not found")
    return _db[id]


@router.post("/", response_model=GeneralIntel, status_code=201)
def create(item: GeneralIntel):
    item.id = str(uuid4())
    _db[item.id] = item
    return item


@router.put("/{id}", response_model=GeneralIntel)
def update(id: str, item: GeneralIntel):
    if id not in _db:
        raise HTTPException(status_code=404, detail="GeneralIntel not found")
    item.id = id
    _db[id] = item
    return item


@router.delete("/{id}", status_code=204)
def delete(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="GeneralIntel not found")
    del _db[id]
