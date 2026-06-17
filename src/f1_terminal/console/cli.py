"""``f1term`` command-line interface (Typer).

Subcommands: ``serve`` (launch the API), ``repl`` (interactive console), and
one-shot data commands that mirror the REPL.
"""
from __future__ import annotations

from typing import Optional

import typer

from f1_terminal.console import commands

app = typer.Typer(
    help="F1 Terminal — command console & server launcher.",
    no_args_is_help=True,
    add_completion=False,
)


@app.command()
def serve(host: str = "127.0.0.1", port: int = 8000, reload: bool = False) -> None:
    """Launch the FastAPI server (uvicorn)."""
    import uvicorn

    uvicorn.run("f1_terminal.api.app:app", host=host, port=port, reload=reload)


@app.command()
def repl() -> None:
    """Start the interactive command console."""
    from f1_terminal.console.repl import run_repl

    run_repl()


@app.command()
def sessions(season: int, round: Optional[int] = None) -> None:
    """List sessions for a season."""
    commands.cmd_sessions(season, round)


@app.command()
def laps(session_id: str, driver: Optional[str] = None) -> None:
    """Lap times for a session (driver = a code like VER or a full driver_id)."""
    commands.cmd_laps(session_id, driver)


@app.command()
def stints(session_id: str) -> None:
    """Per-stint tire summary for a session."""
    commands.cmd_stints(session_id)



if __name__ == "__main__":
    app()
