from typing import List, Optional
from fastapi import APIRouter, HTTPException
from api.pydantic_mode.human_source import HumanSource

router = APIRouter(prefix="/human-sources", tags=["Human Sources"])
_db: dict[int, HumanSource] = {}
_counter = 0


def _next_id() -> int:
    global _counter
    _counter += 1
    return _counter


@router.get("/", response_model=List[HumanSource])
def list_all(
    name: Optional[str] = None,
    for_name: Optional[str] = None,
):
    items = list(_db.values())
    if name:
        items = [i for i in items if name.lower() in i.name.lower()]
    if for_name:
        items = [i for i in items if for_name.lower() in i.for_name.lower()]
    return items


@router.get("/{id}", response_model=HumanSource)
def get_one(id: int):
    if id not in _db:
        raise HTTPException(status_code=404, detail="HumanSource not found")
    return _db[id]


@router.post("/", response_model=HumanSource, status_code=201)
def create(item: HumanSource):
    item.id = _next_id()
    _db[item.id] = item
    return item


@router.put("/{id}", response_model=HumanSource)
def update(id: int, item: HumanSource):
    if id not in _db:
        raise HTTPException(status_code=404, detail="HumanSource not found")
    item.id = id
    _db[id] = item
    return item


@router.delete("/{id}", status_code=204)
def delete(id: int):
    if id not in _db:
        raise HTTPException(status_code=404, detail="HumanSource not found")
    del _db[id]
