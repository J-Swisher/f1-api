"""Rich table rendering for the CLI and REPL.

Styled for PowerShell / Windows Terminal (rich enables VT processing and falls
back through colorama on legacy consoles — both are installed). Data arrives
already-shaped from f1db; here we only handle *visual* formatting.
"""
from __future__ import annotations

import sys
from typing import Any, Sequence

from rich.console import Console
from rich.table import Table
from rich.text import Text

# Emit UTF-8 so rich's box glyphs + symbols render on Windows consoles.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):  # non-reconfigurable stream (e.g. pytest capture)
    pass

console = Console()

# Tyre-compound colours.
_COMPOUND_STYLE = {
    "SOFT": "bold red", "MEDIUM": "bold yellow", "HARD": "bold bright_white",
    "INTER": "bold green", "WET": "bold blue",
}
# Columns rendered as race times (ms -> m:ss.mmm).
_TIME_COLS = {"lap_time_ms", "median_clean_lap_ms", "duration_ms", "fastest_lap_time_ms"}
# Right-aligned numeric columns.
_NUMERIC_COLS = _TIME_COLS | {
    "lap_number", "stint_number", "tyre_age_laps", "tyre_age_start", "tyre_age_end",
    "lap_start", "lap_end", "lap_count", "sector1_ms", "sector2_ms", "sector3_ms",
    "round", "season", "driver_number", "finish_position", "grid_position", "points",
}


def _fmt_ms(value: int) -> str:
    """78065 -> '1:18.065'."""
    secs, ms = divmod(int(value), 1000)
    minutes, secs = divmod(secs, 60)
    return f"{minutes}:{secs:02d}.{ms:03d}"


def _cell(column: str, value: Any) -> Text | str:
    if value is None:
        return Text("·", style="dim")
    if isinstance(value, bool):
        return Text("✓", style="green") if value else Text("", style="dim")
    if column in _TIME_COLS:
        return _fmt_ms(value)
    if column == "compound":
        return Text(str(value), style=_COMPOUND_STYLE.get(str(value), "white"))
    return str(value)


def render_table(
    rows: Sequence[dict[str, Any]], columns: Sequence[str], title: str | None = None
) -> None:
    """Render ``rows`` (showing only ``columns``) as a styled rich table."""
    if not rows:
        console.print("[dim](no rows)[/dim]")
        return
    table = Table(
        title=title,
        header_style="bold cyan",
        title_style="bold magenta",
        border_style="grey37",
        row_styles=["", "on grey11"],
    )
    for column in columns:
        table.add_column(column, justify="right" if column in _NUMERIC_COLS else "left", no_wrap=True)
    for row in rows:
        table.add_row(*[_cell(column, row.get(column)) for column in columns])
    console.print(table)
    console.print(f"[dim]({len(rows)} rows)[/dim]")
