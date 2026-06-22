"""Smoke tests for the endpoints backing the first 4 frontend components."""
from __future__ import annotations

from fastapi.testclient import TestClient

from f1_terminal.api.app import app

client = TestClient(app)


def test_results_endpoint(session_id: str) -> None:
    """Component 2: race results (existing db fn, newly routed)."""
    resp = client.get(f"/sessions/{session_id}/results")
    assert resp.status_code == 200
    body = resp.json()
    assert body and {"driver_id", "finish_position", "points"} <= body[0].keys()


def test_driver_endpoint(session_id: str) -> None:
    """Component 1: single driver profile. driver_id is taken from the session laps."""
    laps = client.get(f"/sessions/{session_id}/laps").json()
    driver_id = laps[0]["driver_id"]

    resp = client.get(f"/drivers/{driver_id}")
    assert resp.status_code == 200
    body = resp.json()
    assert body["driver_id"] == driver_id
    assert {"forename", "surname", "team_name"} <= body.keys()


def test_driver_endpoint_404() -> None:
    assert client.get("/drivers/not_a_real_driver_9999").status_code == 404


def test_driver_summary_endpoint(session_id: str) -> None:
    """Component 2 (driver grain). Gated on the f1-db feature: 501 until shipped,
    200 with the shared analytic vocabulary once it is."""
    resp = client.get(f"/sessions/{session_id}/driver-summary")
    assert resp.status_code in (200, 501)
    if resp.status_code == 200:
        body = resp.json()
        assert body and {"driver_id", "fastest_lap_time_ms", "stint_count"} <= body[0].keys()
