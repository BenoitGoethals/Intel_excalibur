from typing import List, Optional
from sqlalchemy.orm import Session
from model.orm.in_sum_orm import InSumOrm
from repo.base_repo import BaseRepo


class InSumRepo(BaseRepo[InSumOrm]):
    def __init__(self) -> None:
        super().__init__(InSumOrm)

    def get_filtered(
        self,
        db: Session,
        name: Optional[str] = None,
        reporting_agency: Optional[str] = None,
        short_description: Optional[str] = None,
    ) -> List[InSumOrm]:
        q = db.query(InSumOrm)
        if name:
            q = q.filter(InSumOrm.name.ilike(f"%{name}%"))
        if reporting_agency:
            q = q.filter(InSumOrm.reporting_agency.ilike(f"%{reporting_agency}%"))
        if short_description:
            q = q.filter(InSumOrm.short_description.ilike(f"%{short_description}%"))
        return q.all()


in_sum_repo = InSumRepo()
