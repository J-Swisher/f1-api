"""Response model for race results."""
from __future__ import annotations

from pydantic import BaseModel


class ResultOut(BaseModel):
    result_id: int
    session_id: str
    driver_id: str
    forename: str | None = None
    surname: str | None = None
    code: str | None = None
    finish_position: int | None = None
    grid_position: int | None = None
    status: str | None = None
    points: float | None = None
    fastest_lap: bool | None = None
    fastest_lap_time_ms: int | None = None
