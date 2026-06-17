"""Application-database tables (separate from the read-only f1-db)."""
from __future__ import annotations

from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, Integer, String, Table, Text

from f1_terminal.db.engine import metadata

# Saved terminal layouts (Bloomberg-Launchpad style). `layout_json` is an opaque
# blob owned by the frontend; the backend just persists and returns it.
workspace = Table(
    "workspace",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String, nullable=False, unique=True),
    Column("layout_json", Text, nullable=False, default="{}"),
    Column(
        "created_at",
        DateTime,
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
    ),
)
