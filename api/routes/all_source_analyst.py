from typing import List, Optional
from uuid import uuid4
from fastapi import APIRouter, HTTPException
from api.pydantic_mode.all_source_analyst import AllSourceAnalyst

router = APIRouter(prefix="/all-source-analysts", tags=["All-Source Analysts"])
_db: dict[str, AllSourceAnalyst] = {}


@router.get("/", response_model=List[AllSourceAnalyst])
def list_all(
    name: Optional[str] = None,
    unit: Optional[str] = None,
    current_case_file_id: Optional[str] = None,
    active: Optional[bool] = None,
):
    items = list(_db.values())
    if name:
        items = [i for i in items if name.lower() in i.name.lower()]
    if unit:
        items = [i for i in items if i.unit and unit.lower() in i.unit.lower()]
    if current_case_file_id:
        items = [i for i in items if i.current_case_file_id == current_case_file_id]
    if active is not None:
        items = [i for i in items if i.active == active]
    return items


@router.get("/{id}", response_model=AllSourceAnalyst)
def get_one(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="AllSourceAnalyst not found")
    return _db[id]


@router.post("/", response_model=AllSourceAnalyst, status_code=201)
def create(item: AllSourceAnalyst):
    item.id = str(uuid4())
    _db[item.id] = item
    return item


@router.put("/{id}", response_model=AllSourceAnalyst)
def update(id: str, item: AllSourceAnalyst):
    if id not in _db:
        raise HTTPException(status_code=404, detail="AllSourceAnalyst not found")
    item.id = id
    _db[id] = item
    return item


@router.delete("/{id}", status_code=204)
def delete(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="AllSourceAnalyst not found")
    del _db[id]
