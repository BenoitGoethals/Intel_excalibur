from typing import List, Optional
from sqlalchemy.orm import Session
from model.orm.intel_document_orm import IntelDocumentOrm
from repo.base_repo import BaseRepo


class IntelDocumentRepo(BaseRepo[IntelDocumentOrm]):
    def __init__(self) -> None:
        super().__init__(IntelDocumentOrm)

    def get_filtered(
        self,
        db: Session,
        document_type: Optional[str] = None,
        file_name: Optional[str] = None,
    ) -> List[IntelDocumentOrm]:
        q = db.query(IntelDocumentOrm)
        if document_type:
            q = q.filter(IntelDocumentOrm.document_type == document_type)
        if file_name:
            q = q.filter(IntelDocumentOrm.file_name.ilike(f"%{file_name}%"))
        return q.all()


intel_document_repo = IntelDocumentRepo()
