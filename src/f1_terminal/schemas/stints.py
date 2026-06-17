"""Response models for stints and pit stops."""
from __future__ import annotations

from pydantic import BaseModel


class StintOut(BaseModel):
    session_id: str
    driver_id: str
    code: str | None = None
    stint_number: int
    compound: str | None = None
    lap_start: int
    lap_end: int
    lap_count: int
    tyre_age_start: int | None = None
    tyre_age_end: int | None = None
    median_clean_lap_ms: int | None = None


class PitStopOut(BaseModel):
    pit_id: int
    session_id: str
    driver_id: str
    code: str | None = None
    surname: str | None = None
    lap_number: int
    duration_ms: int | None = None
    compound_in: str | None = None
    compound_out: str | None = None
