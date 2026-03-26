from typing import List, Optional
from fastapi import APIRouter, HTTPException
from api.pydantic_mode.operator_intel import OperatorIntel

router = APIRouter(prefix="/operator-intel", tags=["Operator Intel"])
_db: dict[int, OperatorIntel] = {}
_counter = 0


def _next_id() -> int:
    global _counter
    _counter += 1
    return _counter


@router.get("/", response_model=List[OperatorIntel])
def list_all(
    name: Optional[str] = None,
    serial_nbr: Optional[str] = None,
):
    items = list(_db.values())
    if name:
        items = [i for i in items if i.name and name.lower() in i.name.lower()]
    if serial_nbr:
        items = [i for i in items if i.serial_nbr and serial_nbr.lower() in i.serial_nbr.lower()]
    return items


@router.get("/{id}", response_model=OperatorIntel)
def get_one(id: int):
    if id not in _db:
        raise HTTPException(status_code=404, detail="OperatorIntel not found")
    return _db[id]


@router.post("/", response_model=OperatorIntel, status_code=201)
def create(item: OperatorIntel):
    item.id = _next_id()
    _db[item.id] = item
    return item


@router.put("/{id}", response_model=OperatorIntel)
def update(id: int, item: OperatorIntel):
    if id not in _db:
        raise HTTPException(status_code=404, detail="OperatorIntel not found")
    item.id = id
    _db[id] = item
    return item


@router.delete("/{id}", status_code=204)
def delete(id: int):
    if id not in _db:
        raise HTTPException(status_code=404, detail="OperatorIntel not found")
    del _db[id]
