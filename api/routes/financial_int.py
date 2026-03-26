from typing import List, Optional
from fastapi import APIRouter, HTTPException
from api.pydantic_mode.financial_int import FinancialInt

router = APIRouter(prefix="/financial-int", tags=["FININT"])
_db: dict[str, FinancialInt] = {}


@router.get("/", response_model=List[FinancialInt])
def list_all(
    transaction_type: Optional[str] = None,
    counterparty: Optional[str] = None,
    investigation_status: Optional[str] = None,
    investigating_agency: Optional[str] = None,
):
    items = list(_db.values())
    if transaction_type:
        items = [i for i in items if transaction_type.lower() in i.transaction_type.lower()]
    if counterparty:
        items = [i for i in items if counterparty.lower() in i.counterparty.lower()]
    if investigation_status:
        items = [i for i in items if investigation_status.lower() in i.investigation_status.lower()]
    if investigating_agency:
        items = [i for i in items if investigating_agency.lower() in i.investigating_agency.lower()]
    return items


@router.get("/{id}", response_model=FinancialInt)
def get_one(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="FinancialInt not found")
    return _db[id]


@router.post("/", response_model=FinancialInt, status_code=201)
def create(item: FinancialInt):
    _db[item.id] = item
    return item


@router.put("/{id}", response_model=FinancialInt)
def update(id: str, item: FinancialInt):
    if id not in _db:
        raise HTTPException(status_code=404, detail="FinancialInt not found")
    item.id = id
    _db[id] = item
    return item


@router.delete("/{id}", status_code=204)
def delete(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="FinancialInt not found")
    del _db[id]
