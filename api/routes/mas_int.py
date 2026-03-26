from typing import List, Optional
from fastapi import APIRouter, HTTPException
from api.pydantic_mode.mas_int import MasInt

router = APIRouter(prefix="/mas-int", tags=["MASINT"])
_db: dict[str, MasInt] = {}


@router.get("/", response_model=List[MasInt])
def list_all(
    mas_int_type: Optional[str] = None,
    target_name: Optional[str] = None,
    target_location: Optional[str] = None,
):
    items = list(_db.values())
    if mas_int_type:
        items = [i for i in items if i.mas_int_type.value == mas_int_type]
    if target_name:
        items = [i for i in items if target_name.lower() in i.target_name.lower()]
    if target_location:
        items = [i for i in items if target_location.lower() in i.target_location.lower()]
    return items


@router.get("/{id}", response_model=MasInt)
def get_one(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="MasInt not found")
    return _db[id]


@router.post("/", response_model=MasInt, status_code=201)
def create(item: MasInt):
    _db[item.id] = item
    return item


@router.put("/{id}", response_model=MasInt)
def update(id: str, item: MasInt):
    if id not in _db:
        raise HTTPException(status_code=404, detail="MasInt not found")
    item.id = id
    _db[id] = item
    return item


@router.delete("/{id}", status_code=204)
def delete(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="MasInt not found")
    del _db[id]
