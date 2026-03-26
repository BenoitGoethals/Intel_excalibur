from typing import List, Optional
from fastapi import APIRouter, HTTPException
from api.pydantic_mode.intel import Intel

router = APIRouter(prefix="/intel", tags=["Intel"])
_db: dict[int, Intel] = {}
_counter = 0


def _next_id() -> int:
    global _counter
    _counter += 1
    return _counter


@router.get("/", response_model=List[Intel])
def list_all(
    name: Optional[str] = None,
    short_description: Optional[str] = None,
):
    items = list(_db.values())
    if name:
        items = [i for i in items if name.lower() in i.name.lower()]
    if short_description:
        items = [i for i in items if short_description.lower() in i.short_description.lower()]
    return items


@router.get("/{id}", response_model=Intel)
def get_one(id: int):
    if id not in _db:
        raise HTTPException(status_code=404, detail="Intel not found")
    return _db[id]


@router.post("/", response_model=Intel, status_code=201)
def create(item: Intel):
    item.id = _next_id()
    _db[item.id] = item
    return item


@router.put("/{id}", response_model=Intel)
def update(id: int, item: Intel):
    if id not in _db:
        raise HTTPException(status_code=404, detail="Intel not found")
    item.id = id
    _db[id] = item
    return item


@router.delete("/{id}", status_code=204)
def delete(id: int):
    if id not in _db:
        raise HTTPException(status_code=404, detail="Intel not found")
    del _db[id]
