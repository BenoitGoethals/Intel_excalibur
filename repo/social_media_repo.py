from typing import List, Optional
from sqlalchemy.orm import Session
from model.orm.social_media_orm import SocialMediaOrm
from repo.base_repo import BaseRepo


class SocialMediaRepo(BaseRepo[SocialMediaOrm]):
    def __init__(self) -> None:
        super().__init__(SocialMediaOrm)

    def get_filtered(
        self,
        db: Session,
        platform: Optional[str] = None,
        username: Optional[str] = None,
        location: Optional[str] = None,
        private_account: Optional[bool] = None,
    ) -> List[SocialMediaOrm]:
        q = db.query(SocialMediaOrm)
        if platform:
            q = q.filter(SocialMediaOrm.platform.ilike(f"%{platform}%"))
        if username:
            q = q.filter(SocialMediaOrm.username.ilike(f"%{username}%"))
        if location:
            q = q.filter(SocialMediaOrm.location.ilike(f"%{location}%"))
        if private_account is not None:
            q = q.filter(SocialMediaOrm.private_account == private_account)
        return q.all()


social_media_repo = SocialMediaRepo()
