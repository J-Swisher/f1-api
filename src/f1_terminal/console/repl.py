"""Interactive REPL — the Bloomberg-style command line for the F1 terminal.

Dispatches to the same ``commands`` as the CLI; prompt_toolkit drives the input
line (history + tab-completion) and rich renders the output.
"""
from __future__ import annotations

import shlex

from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.history import InMemoryHistory

from f1_terminal.console import commands
from f1_terminal.console._render import console

_HELP = """[bold cyan]commands[/bold cyan]
  [green]sessions[/green] <season> [round]      list sessions for a season
  [green]laps[/green] <session_id> [driver]     lap times (driver = VER or a full driver_id)
  [green]stints[/green] <session_id>            per-stint tire summary
  [green]help[/green]                           show this help
  [green]quit[/green] | [green]exit[/green]                    leave the console"""

_COMMANDS = ["sessions", "laps", "stints", "help", "quit", "exit"]


def _dispatch(line: str) -> bool:
    """Run one console line. Return False to exit the loop."""
    try:
        parts = shlex.split(line)
    except ValueError as exc:
        console.print(f"[red]parse error:[/red] {exc}")
        return True
    if not parts:
        return True
    cmd, *args = parts
    try:
        if cmd in ("quit", "exit"):
            return False
        if cmd == "help":
            console.print(_HELP)
        elif cmd == "sessions":
            commands.cmd_sessions(int(args[0]), int(args[1]) if len(args) > 1 else None)
        elif cmd == "laps":
            commands.cmd_laps(args[0], args[1] if len(args) > 1 else None)
        elif cmd == "stints":
            commands.cmd_stints(args[0])
        else:
            console.print(f"[yellow]unknown command:[/yellow] {cmd!r} (try 'help')")
    except (IndexError, ValueError) as exc:
        console.print(f"[red]bad arguments for {cmd!r}:[/red] {exc} (try 'help')")
    return True


def run_repl() -> None:
    session: PromptSession = PromptSession(
        history=InMemoryHistory(), completer=WordCompleter(_COMMANDS)
    )
    console.print("[bold magenta]F1 Terminal[/bold magenta] console — type [green]help[/green] or [green]quit[/green].")
    while True:
        try:
            line = session.prompt(HTML("<ansicyan><b>f1></b></ansicyan> "))
        except (EOFError, KeyboardInterrupt):
            break
        if not _dispatch(line):
            break
    console.print("[dim]bye.[/dim]")
