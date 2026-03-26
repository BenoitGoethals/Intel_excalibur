from typing import List, Optional
from sqlalchemy.orm import Session
from model.orm.news_article_orm import NewsArticleOrm
from repo.base_repo import BaseRepo


class NewsArticleRepo(BaseRepo[NewsArticleOrm]):
    def __init__(self) -> None:
        super().__init__(NewsArticleOrm)

    def get_filtered(
        self,
        db: Session,
        title: Optional[str] = None,
        author: Optional[str] = None,
        source: Optional[str] = None,
        keyword: Optional[str] = None,
    ) -> List[NewsArticleOrm]:
        q = db.query(NewsArticleOrm)
        if title:
            q = q.filter(NewsArticleOrm.title.ilike(f"%{title}%"))
        if author:
            q = q.filter(NewsArticleOrm.author.ilike(f"%{author}%"))
        if source:
            q = q.filter(NewsArticleOrm.source.ilike(f"%{source}%"))
        if keyword:
            q = q.filter(NewsArticleOrm.keywords.contains(keyword))
        return q.all()


news_article_repo = NewsArticleRepo()
