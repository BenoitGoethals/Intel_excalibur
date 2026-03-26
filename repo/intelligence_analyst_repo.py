from typing import List, Optional
from sqlalchemy.orm import Session
from model.orm.intelligence_analyst_orm import IntelligenceAnalystOrm
from repo.base_repo import BaseRepo


class IntelligenceAnalystRepo(BaseRepo[IntelligenceAnalystOrm]):
    def __init__(self) -> None:
        super().__init__(IntelligenceAnalystOrm)

    def get_filtered(
        self,
        db: Session,
        name: Optional[str] = None,
        specialization: Optional[str] = None,
        unit: Optional[str] = None,
        active: Optional[bool] = None,
    ) -> List[IntelligenceAnalystOrm]:
        q = db.query(IntelligenceAnalystOrm)
        if name:
            q = q.filter(IntelligenceAnalystOrm.name.ilike(f"%{name}%"))
        if specialization:
            q = q.filter(IntelligenceAnalystOrm.specialization.ilike(f"%{specialization}%"))
        if unit:
            q = q.filter(IntelligenceAnalystOrm.unit.ilike(f"%{unit}%"))
        if active is not None:
            q = q.filter(IntelligenceAnalystOrm.active == active)
        return q.all()


intelligence_analyst_repo = IntelligenceAnalystRepo()
