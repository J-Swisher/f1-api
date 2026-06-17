"""Response model for a single lap (mirrors f1db ``fact_lap``)."""
from __future__ import annotations

from pydantic import BaseModel


class LapOut(BaseModel):
    lap_id: int
    session_id: str
    driver_id: str
    # joined in by the f1db v_lap view
    code: str | None = None
    surname: str | None = None
    team_name: str | None = None
    lap_number: int
    lap_time_ms: int | None = None
    sector1_ms: int | None = None
    sector2_ms: int | None = None
    sector3_ms: int | None = None
    speed_i1_kph: float | None = None
    speed_i2_kph: float | None = None
    speed_fl_kph: float | None = None
    speed_st_kph: float | None = None
    compound: str | None = None
    tyre_age_laps: int | None = None
    is_pit_out_lap: bool | None = None
    is_pit_in_lap: bool | None = None
    deleted: bool | None = None
    # derived in the view
    stint_number: int | None = None
    is_clean_racing_lap: bool | None = None
