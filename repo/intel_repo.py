from typing import List, Optional
from sqlalchemy.orm import Session
from model.orm.intel_orm import IntelOrm
from repo.base_repo import BaseRepo


class IntelRepo(BaseRepo[IntelOrm]):
    def __init__(self) -> None:
        super().__init__(IntelOrm)

    def get_filtered(
        self,
        db: Session,
        name: Optional[str] = None,
        short_description: Optional[str] = None,
    ) -> List[IntelOrm]:
        q = db.query(IntelOrm)
        if name:
            q = q.filter(IntelOrm.name.ilike(f"%{name}%"))
        if short_description:
            q = q.filter(IntelOrm.short_description.ilike(f"%{short_description}%"))
        return q.all()


intel_repo = IntelRepo()
