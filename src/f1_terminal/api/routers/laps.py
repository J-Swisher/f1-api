"""Lap-time endpoints."""
from __future__ import annotations

from fastapi import APIRouter

from f1_terminal.schemas.laps import LapOut
from f1_terminal.services import laps as svc

router = APIRouter(tags=["laps"])


@router.get("/sessions/{session_id}/laps", response_model=list[LapOut])
def session_laps(session_id: str, driver_id: str | None = None) -> list[dict]:
    return svc.get_session_laps(session_id, driver_id=driver_id)
