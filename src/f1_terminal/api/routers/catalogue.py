"""Catalogue endpoints: seasons, events, drivers, sessions."""
from __future__ import annotations

from typing import Any

from fastapi import APIRouter

from f1_terminal.services import catalogue as svc

router = APIRouter(tags=["catalogue"])


@router.get("/seasons")
def seasons() -> list[dict[str, Any]]:
    return svc.get_seasons()


@router.get("/seasons/{year}/events")
def events(year: int) -> list[dict[str, Any]]:
    return svc.get_events(year)


@router.get("/seasons/{year}/drivers")
def drivers(year: int) -> list[dict[str, Any]]:
    return svc.get_drivers(year)


@router.get("/sessions")
def sessions(season: int, round: int | None = None) -> list[dict[str, Any]]:
    return svc.get_sessions(season, round=round)
