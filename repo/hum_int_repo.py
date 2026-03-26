from typing import List, Optional
from sqlalchemy.orm import Session
from model.orm.hum_int_orm import HumIntOrm
from repo.base_repo import BaseRepo


class HumIntRepo(BaseRepo[HumIntOrm]):
    def __init__(self) -> None:
        super().__init__(HumIntOrm)

    def get_filtered(
        self,
        db: Session,
        source_name: Optional[str] = None,
        hum_int_type: Optional[str] = None,
        operational_status: Optional[str] = None,
        source_affiliation: Optional[str] = None,
    ) -> List[HumIntOrm]:
        q = db.query(HumIntOrm)
        if source_name:
            q = q.filter(HumIntOrm.source_name.ilike(f"%{source_name}%"))
        if hum_int_type:
            q = q.filter(HumIntOrm.hum_int_type == hum_int_type)
        if operational_status:
            q = q.filter(HumIntOrm.operational_status.ilike(f"%{operational_status}%"))
        if source_affiliation:
            q = q.filter(HumIntOrm.source_affiliation.ilike(f"%{source_affiliation}%"))
        return q.all()


hum_int_repo = HumIntRepo()
