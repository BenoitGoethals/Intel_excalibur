from typing import List, Optional
from sqlalchemy.orm import Session
from model.orm.person_of_interest_orm import PersonOfInterestOrm
from repo.base_repo import BaseRepo


class PersonOfInterestRepo(BaseRepo[PersonOfInterestOrm]):
    def __init__(self) -> None:
        super().__init__(PersonOfInterestOrm)

    def get_filtered(
        self,
        db: Session,
        name: Optional[str] = None,
        alias: Optional[str] = None,
        nationality: Optional[str] = None,
        political_group: Optional[str] = None,
        min_threat_level: Optional[int] = None,
        max_threat_level: Optional[int] = None,
    ) -> List[PersonOfInterestOrm]:
        q = db.query(PersonOfInterestOrm)
        if name:
            q = q.filter(PersonOfInterestOrm.name.ilike(f"%{name}%"))
        if alias:
            q = q.filter(PersonOfInterestOrm.alias.ilike(f"%{alias}%"))
        if nationality:
            q = q.filter(PersonOfInterestOrm.nationality.ilike(f"%{nationality}%"))
        if political_group:
            q = q.filter(PersonOfInterestOrm.political_group.ilike(f"%{political_group}%"))
        if min_threat_level is not None:
            q = q.filter(PersonOfInterestOrm.threat_level >= min_threat_level)
        if max_threat_level is not None:
            q = q.filter(PersonOfInterestOrm.threat_level <= max_threat_level)
        return q.all()


person_of_interest_repo = PersonOfInterestRepo()
