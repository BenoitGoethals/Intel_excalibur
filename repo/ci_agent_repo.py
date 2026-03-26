from typing import List, Optional
from sqlalchemy.orm import Session
from model.orm.ci_agent_orm import CIAgentOrm
from repo.base_repo import BaseRepo


class CIAgentRepo(BaseRepo[CIAgentOrm]):
    def __init__(self) -> None:
        super().__init__(CIAgentOrm)

    def get_filtered(
        self,
        db: Session,
        name: Optional[str] = None,
        ci_specialty: Optional[str] = None,
        unit: Optional[str] = None,
        active: Optional[bool] = None,
        undercover: Optional[bool] = None,
    ) -> List[CIAgentOrm]:
        q = db.query(CIAgentOrm)
        if name:
            q = q.filter(CIAgentOrm.name.ilike(f"%{name}%"))
        if ci_specialty:
            q = q.filter(CIAgentOrm.ci_specialty.ilike(f"%{ci_specialty}%"))
        if unit:
            q = q.filter(CIAgentOrm.unit.ilike(f"%{unit}%"))
        if active is not None:
            q = q.filter(CIAgentOrm.active == active)
        if undercover is not None:
            q = q.filter(CIAgentOrm.undercover == undercover)
        return q.all()


ci_agent_repo = CIAgentRepo()
