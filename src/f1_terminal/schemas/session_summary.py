"""Response model for the per-driver session summary (component 2, driver grain).

One row per driver in a session. The analytic columns share the same vocabulary
as the stint grain (StintOut) so the frontend can render driver -> stint rows with
one column set. Every analytic field is optional: f1-db populates what it can and
leaves the rest null rather than the API synthesizing anything.
"""
from __future__ import annotations

from pydantic import BaseModel


class DriverSummaryOut(BaseModel):
    session_id: str
    driver_id: str
    code: str | None = None
    team_name: str | None = None
    # shared analytic vocabulary (driver grain)
    fastest_lap_time_ms: int | None = None
    median_clean_lap_ms: int | None = None
    lap_count: int | None = None
    pit_stop_count: int | None = None
    stint_count: int | None = None
    # race result fields
    finish_position: int | None = None
    grid_position: int | None = None
    points: float | None = None
    status: str | None = None
