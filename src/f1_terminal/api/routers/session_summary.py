"""Per-driver session summary endpoint (component 2, driver grain)."""
from __future__ import annotations

from fastapi import APIRouter, HTTPException

from f1_terminal.schemas.session_summary import DriverSummaryOut
from f1_terminal.services import session_summary as svc

router = APIRouter(tags=["session-summary"])


@router.get("/sessions/{session_id}/driver-summary", response_model=list[DriverSummaryOut])
def session_driver_summary(session_id: str) -> list[dict]:
    try:
        return svc.get_session_driver_summary(session_id)
    except NotImplementedError as exc:
        raise HTTPException(status_code=501, detail=str(exc)) from exc
