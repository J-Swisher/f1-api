"""Response model for a single driver profile (from the v_driver view)."""
from __future__ import annotations

import datetime as dt

from pydantic import BaseModel


class DriverOut(BaseModel):
    driver_id: str
    profile_id: str | None = None
    team_id: str | None = None
    season: int
    driver_number: int | None = None
    forename: str | None = None
    surname: str | None = None
    code: str | None = None
    nationality: str | None = None
    dob: dt.date | None = None
    permanent_number: int | None = None
    constructor_id: str | None = None
    team_name: str | None = None
