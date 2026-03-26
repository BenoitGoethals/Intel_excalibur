from typing import List, Optional
from sqlalchemy.orm import Session
from model.orm.all_source_analyst_orm import AllSourceAnalystOrm
from repo.base_repo import BaseRepo


class AllSourceAnalystRepo(BaseRepo[AllSourceAnalystOrm]):
    def __init__(self) -> None:
        super().__init__(AllSourceAnalystOrm)

    def get_filtered(
        self,
        db: Session,
        name: Optional[str] = None,
        unit: Optional[str] = None,
        current_case_file_id: Optional[str] = None,
        active: Optional[bool] = None,
    ) -> List[AllSourceAnalystOrm]:
        q = db.query(AllSourceAnalystOrm)
        if name:
            q = q.filter(AllSourceAnalystOrm.name.ilike(f"%{name}%"))
        if unit:
            q = q.filter(AllSourceAnalystOrm.unit.ilike(f"%{unit}%"))
        if current_case_file_id:
            q = q.filter(AllSourceAnalystOrm.current_case_file_id == current_case_file_id)
        if active is not None:
            q = q.filter(AllSourceAnalystOrm.active == active)
        return q.all()


all_source_analyst_repo = AllSourceAnalystRepo()
