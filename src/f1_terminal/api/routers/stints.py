"""Stint + pit-stop endpoints."""
from __future__ import annotations

from fastapi import APIRouter

from f1_terminal.schemas.stints import PitStopOut, StintOut
from f1_terminal.services import stints as svc

router = APIRouter(tags=["stints"])


@router.get("/sessions/{session_id}/stints", response_model=list[StintOut])
def session_stints(session_id: str) -> list[dict]:
    return svc.get_stints(session_id)


@router.get("/sessions/{session_id}/pit-stops", response_model=list[PitStopOut])
def session_pit_stops(session_id: str) -> list[dict]:
    return svc.get_pit_stops(session_id)
