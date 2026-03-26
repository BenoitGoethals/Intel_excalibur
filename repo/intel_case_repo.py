from typing import List, Optional
from sqlalchemy.orm import Session
from model.orm.intel_case_orm import IntelCaseOrm
from repo.base_repo import BaseRepo


class IntelCaseRepo(BaseRepo[IntelCaseOrm]):
    def __init__(self) -> None:
        super().__init__(IntelCaseOrm)

    def get_filtered(
        self,
        db: Session,
        title: Optional[str] = None,
        case_number: Optional[str] = None,
        status: Optional[str] = None,
        priority: Optional[str] = None,
        case_officer_id: Optional[str] = None,
    ) -> List[IntelCaseOrm]:
        q = db.query(IntelCaseOrm)
        if title:
            q = q.filter(IntelCaseOrm.title.ilike(f"%{title}%"))
        if case_number:
            q = q.filter(IntelCaseOrm.case_number.ilike(f"%{case_number}%"))
        if status:
            q = q.filter(IntelCaseOrm.status == status)
        if priority:
            q = q.filter(IntelCaseOrm.priority == priority)
        if case_officer_id:
            q = q.filter(IntelCaseOrm.case_officer_id == case_officer_id)
        return q.all()


intel_case_repo = IntelCaseRepo()
