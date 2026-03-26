from contextlib import contextmanager
from typing import Any, Generator, Generic, List, Optional, Type, TypeVar
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from model.orm.base import Base

T = TypeVar("T", bound=Base)


class BaseRepo(Generic[T]):
    """
    Generic CRUD repository with explicit transaction support.

    All write methods (create / update / delete) do NOT auto-commit so that
    multiple repo calls can participate in a single caller-owned transaction.

    Use the `transaction()` context manager to wrap a unit of work:

        with repo.transaction(db):
            repo.create(db, obj_a)
            other_repo.create(db, obj_b)
        # committed here, or rolled back on exception

    For read-only operations no transaction wrapper is required.
    """

    def __init__(self, model: Type[T]) -> None:
        self.model = model

    # ------------------------------------------------------------------
    # Transaction helpers
    # ------------------------------------------------------------------

    @staticmethod
    @contextmanager
    def transaction(db: Session) -> Generator[Session, None, None]:
        """
        Context manager that commits on success and rolls back on any error.

        Example::

            with BaseRepo.transaction(db) as session:
                repo_a.create(session, obj_a)
                repo_b.update(session, id_b, data_b)
        """
        try:
            yield db
            db.commit()
        except SQLAlchemyError:
            db.rollback()
            raise
        except Exception:
            db.rollback()
            raise

    # ------------------------------------------------------------------
    # Read operations  (no transaction needed)
    # ------------------------------------------------------------------

    def get_by_id(self, db: Session, id: Any) -> Optional[T]:
        return db.get(self.model, id)

    def get_all(self, db: Session) -> List[T]:
        return db.query(self.model).all()

    # ------------------------------------------------------------------
    # Write operations  (caller must wrap in transaction())
    # ------------------------------------------------------------------

    def create(self, db: Session, obj: T) -> T:
        db.add(obj)
        db.flush()       # sends INSERT; assigns server-generated PKs
        db.refresh(obj)  # reload to get DB defaults
        return obj

    def update(self, db: Session, id: Any, data: dict) -> Optional[T]:
        obj = db.get(self.model, id)
        if obj is None:
            return None
        for key, value in data.items():
            if hasattr(obj, key):
                setattr(obj, key, value)
        db.flush()
        db.refresh(obj)
        return obj

    def delete(self, db: Session, id: Any) -> bool:
        obj = db.get(self.model, id)
        if obj is None:
            return False
        db.delete(obj)
        db.flush()
        return True

    # ------------------------------------------------------------------
    # Convenience: single-object write wrapped in its own transaction
    # ------------------------------------------------------------------

    def create_commit(self, db: Session, obj: T) -> T:
        with self.transaction(db):
            return self.create(db, obj)

    def update_commit(self, db: Session, id: Any, data: dict) -> Optional[T]:
        with self.transaction(db):
            return self.update(db, id, data)

    def delete_commit(self, db: Session, id: Any) -> bool:
        with self.transaction(db):
            return self.delete(db, id)
