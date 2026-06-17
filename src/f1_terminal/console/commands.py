"""Console commands shared by the Typer CLI and the REPL.

Each command fetches via the services layer and renders a rich table — keeping
the CLI and REPL identical.
"""
from __future__ import annotations

from f1_terminal.console._render import render_table
from f1_terminal.services import catalogue as catalogue_svc
from f1_terminal.services import laps as laps_svc
from f1_terminal.services import stints as stints_svc

_SESSION_COLS = ["session_id", "session_type", "event_name", "circuit_name", "session_date"]
_LAP_COLS = [
    "code", "driver_id", "lap_number", "stint_number", "lap_time_ms", "compound",
    "tyre_age_laps", "is_pit_out_lap", "is_pit_in_lap",
]
_STINT_COLS = [
    "code", "driver_id", "stint_number", "compound", "lap_start", "lap_end",
    "lap_count", "tyre_age_end", "median_clean_lap_ms",
]


def cmd_sessions(season: int, round: int | None = None) -> None:
    title = f"Sessions — {season}" + (f" R{round}" if round else "")
    render_table(catalogue_svc.get_sessions(season, round=round), _SESSION_COLS, title=title)


def cmd_laps(session_id: str, driver: str | None = None) -> None:
    driver_id = laps_svc.resolve_driver_id(session_id, driver)
    title = f"Laps — {session_id}" + (f" · {driver}" if driver else "")
    render_table(laps_svc.get_session_laps(session_id, driver_id=driver_id), _LAP_COLS, title=title)


def cmd_stints(session_id: str) -> None:
    render_table(stints_svc.get_stints(session_id), _STINT_COLS, title=f"Stints — {session_id}")
