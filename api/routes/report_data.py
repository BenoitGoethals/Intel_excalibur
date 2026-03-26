from typing import List, Optional
from fastapi import APIRouter, HTTPException
from api.pydantic_mode.report_data import ReportData

router = APIRouter(prefix="/report-data", tags=["Report Data"])
_db: dict[int, ReportData] = {}
_counter = 0


def _next_id() -> int:
    global _counter
    _counter += 1
    return _counter


@router.get("/", response_model=List[ReportData])
def list_all(
    type_base_line: Optional[str] = None,
    min_count: Optional[int] = None,
):
    items = list(_db.values())
    if type_base_line:
        items = [i for i in items if i.type_base_line.value == type_base_line]
    if min_count is not None:
        items = [i for i in items if i.count >= min_count]
    return items


@router.get("/{id}", response_model=ReportData)
def get_one(id: int):
    if id not in _db:
        raise HTTPException(status_code=404, detail="ReportData not found")
    return _db[id]


@router.post("/", response_model=ReportData, status_code=201)
def create(item: ReportData):
    item.id = _next_id()
    _db[item.id] = item
    return item


@router.put("/{id}", response_model=ReportData)
def update(id: int, item: ReportData):
    if id not in _db:
        raise HTTPException(status_code=404, detail="ReportData not found")
    item.id = id
    _db[id] = item
    return item


@router.delete("/{id}", status_code=204)
def delete(id: int):
    if id not in _db:
        raise HTTPException(status_code=404, detail="ReportData not found")
    del _db[id]
