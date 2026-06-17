from __future__ import annotations

from typing import Any

from f1db.query import client


def get_seasons() -> list[dict[str, Any]]:
    return client.get_seasons()


def get_events(year: int) -> list[dict[str, Any]]:
    return client.get_events(year)


def get_drivers(year: int) -> list[dict[str, Any]]:
    return client.get_drivers(year)


def get_sessions(season: int, round: int | None = None) -> list[dict[str, Any]]:
    return client.get_sessions(season, round=round)
