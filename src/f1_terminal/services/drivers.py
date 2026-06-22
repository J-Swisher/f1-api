from __future__ import annotations

from typing import Any

from f1db.query import client


def get_driver(driver_id: str) -> dict[str, Any] | None:
    return client.get_driver(driver_id)
