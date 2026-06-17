from __future__ import annotations

from typing import Any

from f1db.query import client


def get_stints(session_id: str) -> list[dict[str, Any]]:
    return client.get_stints(session_id)


def get_pit_stops(session_id: str) -> list[dict[str, Any]]:
    return client.get_pit_stops(session_id)
