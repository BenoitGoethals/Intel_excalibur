"""
Database configuration for Microsoft SQL Server via pyodbc.

Environment variables
---------------------
DATABASE_URL    Full SQLAlchemy URL (overrides all other vars when set).
MSSQL_SERVER    SQL Server hostname / IP          (default: localhost)
MSSQL_DATABASE  Database name                     (default: IntelExcalibur)
MSSQL_USER      SQL auth username                 (default: "" → Windows auth)
MSSQL_PASSWORD  SQL auth password                 (default: "")
MSSQL_DRIVER    ODBC driver name, URL-encoded     (default: ODBC+Driver+17+for+SQL+Server)

Examples
--------
SQL auth:
  DATABASE_URL=mssql+pyodbc://sa:Pass123@myserver/IntelExcalibur?driver=ODBC+Driver+17+for+SQL+Server

Windows / Azure AD integrated auth:
  DATABASE_URL=mssql+pyodbc://@myserver/IntelExcalibur?driver=ODBC+Driver+17+for+SQL+Server&Trusted_Connection=yes
"""
import os
from sqlalchemy import create_engine, event, Engine
from sqlalchemy.orm import sessionmaker, Session
from model.orm.base import Base

# ---------------------------------------------------------------------------
# Build the connection URL
# ---------------------------------------------------------------------------
_SERVER   = os.getenv("MSSQL_SERVER",   "localhost")
_DATABASE = os.getenv("MSSQL_DATABASE", "IntelExcalibur")
_USER     = os.getenv("MSSQL_USER",     "")
_PASSWORD = os.getenv("MSSQL_PASSWORD", "")
_DRIVER   = os.getenv("MSSQL_DRIVER",   "ODBC+Driver+17+for+SQL+Server")

_auth = f"{_USER}:{_PASSWORD}@" if (_USER and _PASSWORD) else ""

_FALLBACK_SQLITE = "sqlite:///intel_excalibur.db"

DATABASE_URL: str = os.getenv(
    "DATABASE_URL",
    f"mssql+pyodbc://{_auth}{_SERVER}/{_DATABASE}?driver={_DRIVER}",
)

# ---------------------------------------------------------------------------
# Lazy engine — created on first use so that importing this module never
# fails on machines without the ODBC driver installed (e.g., CI, local Mac).
# ---------------------------------------------------------------------------
_engine: Engine | None = None
_SessionLocal: sessionmaker | None = None


def _get_engine() -> Engine:
    global _engine, _SessionLocal
    if _engine is None:
        url = DATABASE_URL
        try:
            _engine = create_engine(
                url,
                fast_executemany=True,   # MSSQL bulk-insert optimisation
                pool_pre_ping=True,      # reconnect after dropped idle connections
                pool_size=10,
                max_overflow=20,
            )
            # Force a connection attempt to detect missing ODBC drivers early
            _engine.connect().close()
        except Exception:
            print(f"[database] MSSQL unavailable, falling back to SQLite ({_FALLBACK_SQLITE})")
            _engine = create_engine(_FALLBACK_SQLITE)

        if url.startswith("mssql"):
            @event.listens_for(_engine, "connect")
            def _enforce_manual_commit(dbapi_conn, _):
                """Disable implicit autocommit so every session is transactional."""
                dbapi_conn.autocommit = False

        _SessionLocal = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=_engine,
        )
    return _engine


def get_session() -> Session:
    """Return a raw session (caller is responsible for commit/rollback/close)."""
    _get_engine()
    return _SessionLocal()


def create_tables() -> None:
    """Create all ORM tables. Call once at application startup."""
    Base.metadata.create_all(bind=_get_engine())


def get_db():
    """
    FastAPI dependency — yields a transactional Session.

    Commits automatically when the request succeeds.
    Rolls back and re-raises on any exception.
    """
    db: Session = get_session()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


# Keep engine / SessionLocal accessible for tests and scripts
engine      = property(lambda _: _get_engine())   # noqa: E731
SessionLocal = property(lambda _: _SessionLocal)  # noqa: E731
