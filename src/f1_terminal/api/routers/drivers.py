"""Driver profile endpoints."""
from __future__ import annotations

from fastapi import APIRouter, HTTPException

from f1_terminal.schemas.drivers import DriverOut
from f1_terminal.services import drivers as svc

router = APIRouter(tags=["drivers"])


@router.get("/drivers/{driver_id}", response_model=DriverOut)
def driver(driver_id: str) -> dict:
    row = svc.get_driver(driver_id)
    if row is None:
        raise HTTPException(status_code=404, detail=f"driver not found: {driver_id}")
    return row
