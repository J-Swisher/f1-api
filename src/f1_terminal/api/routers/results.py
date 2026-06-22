"""Race result endpoints."""
from __future__ import annotations

from fastapi import APIRouter

from f1_terminal.schemas.results import ResultOut
from f1_terminal.services import results as svc

router = APIRouter(tags=["results"])


@router.get("/sessions/{session_id}/results", response_model=list[ResultOut])
def session_results(session_id: str) -> list[dict]:
    return svc.get_session_results(session_id)
