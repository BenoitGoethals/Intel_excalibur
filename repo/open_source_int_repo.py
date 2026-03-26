from typing import List, Optional
from sqlalchemy.orm import Session
from model.orm.open_source_int_orm import OpenSourceIntOrm
from repo.base_repo import BaseRepo


class OpenSourceIntRepo(BaseRepo[OpenSourceIntOrm]):
    def __init__(self) -> None:
        super().__init__(OpenSourceIntOrm)

    def get_filtered(
        self,
        db: Session,
        source_name: Optional[str] = None,
        source_type: Optional[str] = None,
        target_name: Optional[str] = None,
        target_location: Optional[str] = None,
    ) -> List[OpenSourceIntOrm]:
        q = db.query(OpenSourceIntOrm)
        if source_name:
            q = q.filter(OpenSourceIntOrm.source_name.ilike(f"%{source_name}%"))
        if source_type:
            q = q.filter(OpenSourceIntOrm.source_type.ilike(f"%{source_type}%"))
        if target_name:
            q = q.filter(OpenSourceIntOrm.target_name.ilike(f"%{target_name}%"))
        if target_location:
            q = q.filter(OpenSourceIntOrm.target_location.ilike(f"%{target_location}%"))
        return q.all()


open_source_int_repo = OpenSourceIntRepo()
