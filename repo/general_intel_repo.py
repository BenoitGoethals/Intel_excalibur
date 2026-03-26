from typing import List, Optional
from sqlalchemy.orm import Session
from model.orm.general_intel_orm import GeneralIntelOrm
from repo.base_repo import BaseRepo


class GeneralIntelRepo(BaseRepo[GeneralIntelOrm]):
    def __init__(self) -> None:
        super().__init__(GeneralIntelOrm)

    def get_filtered(
        self,
        db: Session,
        name: Optional[str] = None,
        reporting_agency: Optional[str] = None,
        incident_location: Optional[str] = None,
        intel_type: Optional[str] = None,
    ) -> List[GeneralIntelOrm]:
        q = db.query(GeneralIntelOrm)
        if name:
            q = q.filter(GeneralIntelOrm.name.ilike(f"%{name}%"))
        if reporting_agency:
            q = q.filter(GeneralIntelOrm.reporting_agency.ilike(f"%{reporting_agency}%"))
        if incident_location:
            q = q.filter(GeneralIntelOrm.incident_location.ilike(f"%{incident_location}%"))
        if intel_type:
            q = q.filter(GeneralIntelOrm.intel_type == intel_type)
        return q.all()


general_intel_repo = GeneralIntelRepo()
