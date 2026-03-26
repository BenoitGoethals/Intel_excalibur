from typing import List, Optional
from sqlalchemy.orm import Session
from model.orm.informant_orm import InformantOrm
from repo.base_repo import BaseRepo


class InformantRepo(BaseRepo[InformantOrm]):
    def __init__(self) -> None:
        super().__init__(InformantOrm)

    def get_filtered(
        self,
        db: Session,
        informant_role: Optional[str] = None,
        gender: Optional[str] = None,
        active_status: Optional[bool] = None,
        areas_of_expertise: Optional[str] = None,
        min_reliability: Optional[int] = None,
    ) -> List[InformantOrm]:
        q = db.query(InformantOrm)
        if informant_role:
            q = q.filter(InformantOrm.informant_role.ilike(f"%{informant_role}%"))
        if gender:
            q = q.filter(InformantOrm.gender == gender)
        if active_status is not None:
            q = q.filter(InformantOrm.active_status == active_status)
        if areas_of_expertise:
            q = q.filter(InformantOrm.areas_of_expertise.ilike(f"%{areas_of_expertise}%"))
        if min_reliability is not None:
            q = q.filter(InformantOrm.reliability_rating >= min_reliability)
        return q.all()


informant_repo = InformantRepo()
