from typing import List, Optional
from uuid import uuid4
from fastapi import APIRouter, HTTPException
from api.pydantic_mode.intel_document import IntelDocument

router = APIRouter(prefix="/intel-documents", tags=["Intel Documents"])
_db: dict[str, IntelDocument] = {}


@router.get("/", response_model=List[IntelDocument])
def list_all(
    document_type: Optional[str] = None,
    file_name: Optional[str] = None,
    keyword: Optional[str] = None,
):
    items = list(_db.values())
    if document_type:
        items = [i for i in items if i.document_type.value == document_type]
    if file_name:
        items = [i for i in items if i.file_name and file_name.lower() in i.file_name.lower()]
    if keyword:
        items = [i for i in items if keyword.lower() in [k.lower() for k in i.keywords]]
    return items


@router.get("/{id}", response_model=IntelDocument)
def get_one(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="IntelDocument not found")
    return _db[id]


@router.post("/", response_model=IntelDocument, status_code=201)
def create(item: IntelDocument):
    item.id = str(uuid4())
    _db[item.id] = item
    return item


@router.put("/{id}", response_model=IntelDocument)
def update(id: str, item: IntelDocument):
    if id not in _db:
        raise HTTPException(status_code=404, detail="IntelDocument not found")
    item.id = id
    _db[id] = item
    return item


@router.delete("/{id}", status_code=204)
def delete(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="IntelDocument not found")
    del _db[id]
