from typing import List, Optional
from uuid import uuid4
from fastapi import APIRouter, HTTPException
from api.pydantic_mode.ci_agent import CIAgent

router = APIRouter(prefix="/ci-agents", tags=["CI Agents"])
_db: dict[str, CIAgent] = {}


@router.get("/", response_model=List[CIAgent])
def list_all(
    name: Optional[str] = None,
    ci_specialty: Optional[str] = None,
    unit: Optional[str] = None,
    active: Optional[bool] = None,
    undercover: Optional[bool] = None,
):
    items = list(_db.values())
    if name:
        items = [i for i in items if name.lower() in i.name.lower()]
    if ci_specialty:
        items = [i for i in items if i.ci_specialty and ci_specialty.lower() in i.ci_specialty.lower()]
    if unit:
        items = [i for i in items if i.unit and unit.lower() in i.unit.lower()]
    if active is not None:
        items = [i for i in items if i.active == active]
    if undercover is not None:
        items = [i for i in items if i.undercover == undercover]
    return items


@router.get("/{id}", response_model=CIAgent)
def get_one(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="CIAgent not found")
    return _db[id]


@router.post("/", response_model=CIAgent, status_code=201)
def create(item: CIAgent):
    item.id = str(uuid4())
    _db[item.id] = item
    return item


@router.put("/{id}", response_model=CIAgent)
def update(id: str, item: CIAgent):
    if id not in _db:
        raise HTTPException(status_code=404, detail="CIAgent not found")
    item.id = id
    _db[id] = item
    return item


@router.delete("/{id}", status_code=204)
def delete(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="CIAgent not found")
    del _db[id]
