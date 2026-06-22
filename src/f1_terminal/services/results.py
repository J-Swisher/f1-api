from __future__ import annotations

from typing import Any

from f1db.query import client


def get_session_results(session_id: str) -> list[dict[str, Any]]:
    return client.get_session_results(session_id)
