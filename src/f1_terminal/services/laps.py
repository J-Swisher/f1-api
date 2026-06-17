from __future__ import annotations

from typing import Any

from f1db.query import client


def get_session_laps(session_id: str, driver_id: str | None = None) -> list[dict[str, Any]]:
    return client.get_session_laps(session_id, driver_id=driver_id)


def resolve_driver_id(session_id: str, token: str | None) -> str | None:
    return client.resolve_driver_id(session_id, token)
