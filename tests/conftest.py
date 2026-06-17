"""Test configuration.

Point f1db at the user's built data and the app DB at a throwaway file *before*
anything imports f1db / f1_terminal (both read their config at import time).
"""
from __future__ import annotations

import os
import tempfile
from pathlib import Path

# Built f1-db data lives in the sibling clone (the submodule ships code only).
os.environ.setdefault("F1DB_DATA_DIR", r"C:\Users\josep\repos\f1-db\data")
# Keep the app DB out of the repo; a temp file is fine for tests.
os.environ.setdefault("APP_DB_PATH", str(Path(tempfile.gettempdir()) / "f1_terminal_test.db"))

# Ensure the f1db views exist in the target DB (idempotent; data shaping is upstream).
from f1db.db.engine import core_engine  # noqa: E402
from f1db.db.views import create_views  # noqa: E402

create_views(core_engine())

import pytest


@pytest.fixture(scope="session")
def session_id() -> str:
    """A real race session present in the built data (1,349 laps)."""
    return "2025_R10_R"
