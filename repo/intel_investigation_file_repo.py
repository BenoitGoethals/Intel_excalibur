from typing import List, Optional
from sqlalchemy.orm import Session
from model.orm.intel_investigation_file_orm import IntelInvestigationFileOrm
from repo.base_repo import BaseRepo


class IntelInvestigationFileRepo(BaseRepo[IntelInvestigationFileOrm]):
    def __init__(self) -> None:
        super().__init__(IntelInvestigationFileOrm)

    def get_filtered(
        self,
        db: Session,
        case_number: Optional[str] = None,
        investigator_name: Optional[str] = None,
        investigation_status: Optional[str] = None,
    ) -> List[IntelInvestigationFileOrm]:
        q = db.query(IntelInvestigationFileOrm)
        if case_number:
            q = q.filter(IntelInvestigationFileOrm.case_number.ilike(f"%{case_number}%"))
        if investigator_name:
            q = q.filter(IntelInvestigationFileOrm.investigator_name.ilike(f"%{investigator_name}%"))
        if investigation_status:
            q = q.filter(IntelInvestigationFileOrm.investigation_status == investigation_status)
        return q.all()


intel_investigation_file_repo = IntelInvestigationFileRepo()
