"""API smoke tests via FastAPI TestClient."""
from __future__ import annotations

from fastapi.testclient import TestClient

from f1_terminal.api.app import app

client = TestClient(app)


def test_health() -> None:
    assert client.get("/health").json() == {"status": "ok"}


def test_laps_endpoint(session_id: str) -> None:
    resp = client.get(f"/sessions/{session_id}/laps")
    assert resp.status_code == 200
    body = resp.json()
    # Enriched upstream by the v_lap view: driver code + derived stint_number.
    assert body and {"driver_id", "lap_number", "code", "stint_number"} <= body[0].keys()


def test_stints_endpoint(session_id: str) -> None:
    resp = client.get(f"/sessions/{session_id}/stints")
    assert resp.status_code == 200
    body = resp.json()
    assert body and "compound" in body[0] and body[0]["stint_number"] == 1


