from typing import List, Optional
from uuid import uuid4
from fastapi import APIRouter, HTTPException
from api.pydantic_mode.news_article import NewsArticle

router = APIRouter(prefix="/news-articles", tags=["News Articles"])
_db: dict[str, NewsArticle] = {}


@router.get("/", response_model=List[NewsArticle])
def list_all(
    title: Optional[str] = None,
    author: Optional[str] = None,
    source: Optional[str] = None,
    keyword: Optional[str] = None,
):
    items = list(_db.values())
    if title:
        items = [i for i in items if i.title and title.lower() in i.title.lower()]
    if author:
        items = [i for i in items if i.author and author.lower() in i.author.lower()]
    if source:
        items = [i for i in items if i.source and source.lower() in i.source.lower()]
    if keyword:
        items = [i for i in items if keyword.lower() in [k.lower() for k in i.keywords]]
    return items


@router.get("/{id}", response_model=NewsArticle)
def get_one(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="NewsArticle not found")
    return _db[id]


@router.post("/", response_model=NewsArticle, status_code=201)
def create(item: NewsArticle):
    item.id = str(uuid4())
    _db[item.id] = item
    return item


@router.put("/{id}", response_model=NewsArticle)
def update(id: str, item: NewsArticle):
    if id not in _db:
        raise HTTPException(status_code=404, detail="NewsArticle not found")
    item.id = id
    _db[id] = item
    return item


@router.delete("/{id}", status_code=204)
def delete(id: str):
    if id not in _db:
        raise HTTPException(status_code=404, detail="NewsArticle not found")
    del _db[id]
