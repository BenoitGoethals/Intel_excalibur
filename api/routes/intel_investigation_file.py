from typing import List, Optional
from uuid import uuid4
from fastapi import APIRouter, HTTPException
from api.pydantic_mode.intel_investigation_file import IntelInvestigationFile

router = APIRouter(prefix="/intel-investigations", tags=["Intel Investigations"])
_db: dict[str, IntelInvestigationFile] = {}


@router.get("/", response_model=List[IntelInvestigationFile])
def list_all(
    case_number: Optional[str] = None,
    investigator_name: Optional[str] = None,
    investigation_status: Optional[str] = None,
):
    items = list(_db.values())
    if case_number:
        items = [i for i in items if i.case_number and case_number.lower() in i.case_number.lower()]
    if investigator_name:
        items = [i for i in items if i.investigator_name and investigator_name.lower() in i.investigator_name.lower()]
    if investigation_status:
        items = [i for i in items if i.investigation_status.value == investigation_status]
    return items


@router.get("/{id}", response_model=IntelInvestigationFile)
def get_one(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="IntelInvestigationFile not found")
    return _db[id]


@router.post("/", response_model=IntelInvestigationFile, status_code=201)
def create(item: IntelInvestigationFile):
    item.id = str(uuid4())
    _db[item.id] = item
    return item


@router.put("/{id}", response_model=IntelInvestigationFile)
def update(id: str, item: IntelInvestigationFile):
    if id not in _db:
        raise HTTPException(status_code=404, detail="IntelInvestigationFile not found")
    item.id = id
    _db[id] = item
    return item


@router.delete("/{id}", status_code=204)
def delete(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="IntelInvestigationFile not found")
    del _db[id]
