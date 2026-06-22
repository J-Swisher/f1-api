from __future__ import annotations

from typing import Any

from f1db.query import client


def get_session_driver_summary(session_id: str) -> list[dict[str, Any]]:
    """Pass-through to the db query client's per-driver session summary.

    The aggregation/join lives entirely in f1-db (view or inline SQL). Until that
    feature ships, ``client.get_session_driver_summary`` is absent; surface that as
    NotImplementedError so the router can return a clean 501.
    """
    fn = getattr(client, "get_session_driver_summary", None)
    if fn is None:
        raise NotImplementedError(
            "f1db.query.client.get_session_driver_summary is not implemented yet "
            "(pending f1-db feature request)"
        )
    return fn(session_id)
