"""Engine + schema bootstrap for the terminal's own application database.

Deliberately separate from the read-only f1-db. Stores terminal state — saved
workspaces today; cached model-input snapshots / model runs later.
"""
from __future__ import annotations

from functools import lru_cache

from sqlalchemy import Engine, MetaData, create_engine

from f1_terminal.config import settings

metadata = MetaData()


@lru_cache(maxsize=None)
def app_engine() -> Engine:
    """Tuned SQLite engine for the app DB (cached per-process)."""
    path = settings.app_db_path
    path.parent.mkdir(parents=True, exist_ok=True)
    return create_engine(f"sqlite:///{path}", future=True)


def init_app_db() -> Engine:
    """Create the app database and its tables if absent. Idempotent."""
    engine = app_engine()
    from f1_terminal.db import models  # noqa: F401  -- register tables on `metadata`

    metadata.create_all(engine)
    return engine
