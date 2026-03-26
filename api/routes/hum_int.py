from typing import List, Optional
from uuid import uuid4
from fastapi import APIRouter, HTTPException
from api.pydantic_mode.hum_int import HumInt

router = APIRouter(prefix="/hum-int", tags=["HUMINT"])
_db: dict[str, HumInt] = {}


@router.get("/", response_model=List[HumInt])
def list_all(
    source_name: Optional[str] = None,
    hum_int_type: Optional[str] = None,
    operational_status: Optional[str] = None,
    source_affiliation: Optional[str] = None,
):
    items = list(_db.values())
    if source_name:
        items = [i for i in items if source_name.lower() in i.source_name.lower()]
    if hum_int_type:
        items = [i for i in items if i.hum_int_type.value == hum_int_type]
    if operational_status:
        items = [i for i in items if operational_status.lower() in i.operational_status.lower()]
    if source_affiliation:
        items = [i for i in items if source_affiliation.lower() in i.source_affiliation.lower()]
    return items


@router.get("/{id}", response_model=HumInt)
def get_one(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="HumInt not found")
    return _db[id]


@router.post("/", response_model=HumInt, status_code=201)
def create(item: HumInt):
    item.id = str(uuid4())
    _db[item.id] = item
    return item


@router.put("/{id}", response_model=HumInt)
def update(id: str, item: HumInt):
    if id not in _db:
        raise HTTPException(status_code=404, detail="HumInt not found")
    item.id = id
    _db[id] = item
    return item


@router.delete("/{id}", status_code=204)
def delete(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="HumInt not found")
    del _db[id]
