from typing import List, Optional
from fastapi import APIRouter, HTTPException
from api.pydantic_mode.counter_int import CounterInt

router = APIRouter(prefix="/counter-int", tags=["Counter Intelligence"])
_db: dict[str, CounterInt] = {}


@router.get("/", response_model=List[CounterInt])
def list_all(
    operation_name: Optional[str] = None,
    target: Optional[str] = None,
    suspect: Optional[str] = None,
):
    items = list(_db.values())
    if operation_name:
        items = [i for i in items if operation_name.lower() in i.operation_name.lower()]
    if target:
        items = [i for i in items if any(target.lower() in t.lower() for t in i.targets)]
    if suspect:
        items = [i for i in items if any(suspect.lower() in s.lower() for s in i.suspects)]
    return items


@router.get("/{id}", response_model=CounterInt)
def get_one(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="CounterInt not found")
    return _db[id]


@router.post("/", response_model=CounterInt, status_code=201)
def create(item: CounterInt):
    _db[item.id] = item
    return item


@router.put("/{id}", response_model=CounterInt)
def update(id: str, item: CounterInt):
    if id not in _db:
        raise HTTPException(status_code=404, detail="CounterInt not found")
    item.id = id
    _db[id] = item
    return item


@router.delete("/{id}", status_code=204)
def delete(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="CounterInt not found")
    del _db[id]
