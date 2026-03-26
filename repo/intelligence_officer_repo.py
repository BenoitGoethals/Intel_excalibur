from typing import List, Optional
from sqlalchemy.orm import Session
from model.orm.intelligence_officer_orm import IntelligenceOfficerOrm
from repo.base_repo import BaseRepo


class IntelligenceOfficerRepo(BaseRepo[IntelligenceOfficerOrm]):
    def __init__(self) -> None:
        super().__init__(IntelligenceOfficerOrm)

    def get_filtered(
        self,
        db: Session,
        name: Optional[str] = None,
        designation: Optional[str] = None,
        unit: Optional[str] = None,
        active: Optional[bool] = None,
    ) -> List[IntelligenceOfficerOrm]:
        q = db.query(IntelligenceOfficerOrm)
        if name:
            q = q.filter(IntelligenceOfficerOrm.name.ilike(f"%{name}%"))
        if designation:
            q = q.filter(IntelligenceOfficerOrm.designation == designation)
        if unit:
            q = q.filter(IntelligenceOfficerOrm.unit.ilike(f"%{unit}%"))
        if active is not None:
            q = q.filter(IntelligenceOfficerOrm.active == active)
        return q.all()


intelligence_officer_repo = IntelligenceOfficerRepo()
