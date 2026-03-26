from typing import List, Optional
from fastapi import APIRouter, HTTPException
from api.pydantic_mode.gov_source import GovSource

router = APIRouter(prefix="/gov-sources", tags=["Government Sources"])
_db: dict[str, GovSource] = {}


@router.get("/", response_model=List[GovSource])
def list_all(
    source_agency: Optional[str] = None,
    source_type: Optional[str] = None,
    clearance_level: Optional[str] = None,
    operational_status: Optional[str] = None,
):
    items = list(_db.values())
    if source_agency:
        items = [i for i in items if source_agency.lower() in i.source_agency.lower()]
    if source_type:
        items = [i for i in items if source_type.lower() in i.source_type.lower()]
    if clearance_level:
        items = [i for i in items if clearance_level.lower() in i.clearance_level.lower()]
    if operational_status:
        items = [i for i in items if operational_status.lower() in i.operational_status.lower()]
    return items


@router.get("/{id}", response_model=GovSource)
def get_one(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="GovSource not found")
    return _db[id]


@router.post("/", response_model=GovSource, status_code=201)
def create(item: GovSource):
    _db[item.id] = item
    return item


@router.put("/{id}", response_model=GovSource)
def update(id: str, item: GovSource):
    if id not in _db:
        raise HTTPException(status_code=404, detail="GovSource not found")
    item.id = id
    _db[id] = item
    return item


@router.delete("/{id}", status_code=204)
def delete(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="GovSource not found")
    del _db[id]
