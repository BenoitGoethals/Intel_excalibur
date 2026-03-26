from typing import List, Optional
from sqlalchemy.orm import Session
from model.orm.intelligence_collector_orm import IntelligenceCollectorOrm
from repo.base_repo import BaseRepo


class IntelligenceCollectorRepo(BaseRepo[IntelligenceCollectorOrm]):
    def __init__(self) -> None:
        super().__init__(IntelligenceCollectorOrm)

    def get_filtered(
        self,
        db: Session,
        name: Optional[str] = None,
        collection_method: Optional[str] = None,
        unit: Optional[str] = None,
        active: Optional[bool] = None,
    ) -> List[IntelligenceCollectorOrm]:
        q = db.query(IntelligenceCollectorOrm)
        if name:
            q = q.filter(IntelligenceCollectorOrm.name.ilike(f"%{name}%"))
        if collection_method:
            q = q.filter(IntelligenceCollectorOrm.collection_method.ilike(f"%{collection_method}%"))
        if unit:
            q = q.filter(IntelligenceCollectorOrm.unit.ilike(f"%{unit}%"))
        if active is not None:
            q = q.filter(IntelligenceCollectorOrm.active == active)
        return q.all()


intelligence_collector_repo = IntelligenceCollectorRepo()
