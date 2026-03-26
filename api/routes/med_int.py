from typing import List, Optional
from fastapi import APIRouter, HTTPException
from api.pydantic_mode.med_int import MedInt

router = APIRouter(prefix="/med-int", tags=["MEDINT"])
_db: dict[str, MedInt] = {}


@router.get("/", response_model=List[MedInt])
def list_all(
    patient_name: Optional[str] = None,
    diagnosis: Optional[str] = None,
    facility_name: Optional[str] = None,
    facility_location: Optional[str] = None,
):
    items = list(_db.values())
    if patient_name:
        items = [i for i in items if patient_name.lower() in i.patient_name.lower()]
    if diagnosis:
        items = [i for i in items if diagnosis.lower() in i.diagnosis.lower()]
    if facility_name:
        items = [i for i in items if facility_name.lower() in i.facility_name.lower()]
    if facility_location:
        items = [i for i in items if facility_location.lower() in i.facility_location.lower()]
    return items


@router.get("/{id}", response_model=MedInt)
def get_one(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="MedInt not found")
    return _db[id]


@router.post("/", response_model=MedInt, status_code=201)
def create(item: MedInt):
    _db[item.id] = item
    return item


@router.put("/{id}", response_model=MedInt)
def update(id: str, item: MedInt):
    if id not in _db:
        raise HTTPException(status_code=404, detail="MedInt not found")
    item.id = id
    _db[id] = item
    return item


@router.delete("/{id}", status_code=204)
def delete(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="MedInt not found")
    del _db[id]
