from typing import List, Optional
from sqlalchemy.orm import Session
from model.orm.cyb_int_orm import CybIntOrm
from repo.base_repo import BaseRepo


class CybIntRepo(BaseRepo[CybIntOrm]):
    def __init__(self) -> None:
        super().__init__(CybIntOrm)

    def get_filtered(
        self,
        db: Session,
        incident_type: Optional[str] = None,
        attribution: Optional[str] = None,
    ) -> List[CybIntOrm]:
        q = db.query(CybIntOrm)
        if incident_type:
            q = q.filter(CybIntOrm.incident_type == incident_type)
        if attribution:
            q = q.filter(CybIntOrm.attribution.ilike(f"%{attribution}%"))
        return q.all()


cyb_int_repo = CybIntRepo()
