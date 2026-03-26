from typing import List, Optional
from fastapi import APIRouter, HTTPException
from api.pydantic_mode.sig_int import SigInt

router = APIRouter(prefix="/sig-int", tags=["SIGINT"])
_db: dict[str, SigInt] = {}


@router.get("/", response_model=List[SigInt])
def list_all(
    signal_type: Optional[str] = None,
    sender: Optional[str] = None,
    receiver: Optional[str] = None,
    sender_location: Optional[str] = None,
):
    items = list(_db.values())
    if signal_type:
        items = [i for i in items if signal_type.lower() in i.signal_type.lower()]
    if sender:
        items = [i for i in items if sender.lower() in i.sender.lower()]
    if receiver:
        items = [i for i in items if receiver.lower() in i.receiver.lower()]
    if sender_location:
        items = [i for i in items if sender_location.lower() in i.sender_location.lower()]
    return items


@router.get("/{id}", response_model=SigInt)
def get_one(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="SigInt not found")
    return _db[id]


@router.post("/", response_model=SigInt, status_code=201)
def create(item: SigInt):
    _db[item.id] = item
    return item


@router.put("/{id}", response_model=SigInt)
def update(id: str, item: SigInt):
    if id not in _db:
        raise HTTPException(status_code=404, detail="SigInt not found")
    item.id = id
    _db[id] = item
    return item


@router.delete("/{id}", status_code=204)
def delete(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="SigInt not found")
    del _db[id]
