from typing import List, Optional
from uuid import uuid4
from fastapi import APIRouter, HTTPException
from api.pydantic_mode.intel_case import IntelCase, LinkedIntel

router = APIRouter(prefix="/intel-cases", tags=["Intel Cases"])
_db: dict[str, IntelCase] = {}


@router.get("/", response_model=List[IntelCase])
def list_all(
    title: Optional[str] = None,
    case_number: Optional[str] = None,
    status: Optional[str] = None,
    priority: Optional[str] = None,
    case_officer_id: Optional[str] = None,
):
    items = list(_db.values())
    if title:
        items = [i for i in items if title.lower() in i.title.lower()]
    if case_number:
        items = [i for i in items if case_number.lower() in i.case_number.lower()]
    if status:
        items = [i for i in items if i.status.value == status]
    if priority:
        items = [i for i in items if i.priority.value == priority]
    if case_officer_id:
        items = [i for i in items if i.case_officer_id == case_officer_id]
    return items


@router.get("/{id}", response_model=IntelCase)
def get_one(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="IntelCase not found")
    return _db[id]


@router.post("/", response_model=IntelCase, status_code=201)
def create(item: IntelCase):
    item.id = str(uuid4())
    _db[item.id] = item
    return item


@router.put("/{id}", response_model=IntelCase)
def update(id: str, item: IntelCase):
    if id not in _db:
        raise HTTPException(status_code=404, detail="IntelCase not found")
    item.id = id
    _db[id] = item
    return item


@router.delete("/{id}", status_code=204)
def delete(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="IntelCase not found")
    del _db[id]


# ── Sub-resource: manage linked intel items ───────────────────────────────

@router.post("/{id}/linked-intel", response_model=IntelCase)
def add_linked_intel(id: str, ref: LinkedIntel):
    """Attach an intel item (from any collection) to this case."""
    if id not in _db:
        raise HTTPException(status_code=404, detail="IntelCase not found")
    case = _db[id]
    if not any(l.intel_id == ref.intel_id for l in case.linked_intel):
        case.linked_intel.append(ref)
    return case


@router.delete("/{id}/linked-intel/{intel_id}", response_model=IntelCase)
def remove_linked_intel(id: str, intel_id: str):
    """Detach an intel item from this case."""
    if id not in _db:
        raise HTTPException(status_code=404, detail="IntelCase not found")
    case = _db[id]
    case.linked_intel = [l for l in case.linked_intel if l.intel_id != intel_id]
    return case
