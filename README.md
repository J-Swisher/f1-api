# f1-api — F1 Terminal backend

A "Bloomberg terminal for F1": a FastAPI service **and** a command console (REPL)
that serve lap-time and tire/stint data on top of the [`f1-db`](external/f1-db)
dataset. Two consumers drive the first feature: a React frontend, and a separate
(pip-installed) Python package that regresses tire degradation — this backend
serves that package its **model inputs**.

## Layout

```
external/f1-db/          # git submodule: read-only F1 dataset + query client (f1db)
src/f1_terminal/
  config.py              # settings + wires F1DB_* env so f1db finds the data
  services/              # domain logic over f1db.query.client (laps, stints, model inputs)
  schemas/               # Pydantic response models
  api/                   # FastAPI app + routers
  db/                    # the terminal's OWN app database (separate from f1-db)
  console/               # Typer CLI + prompt_toolkit REPL
tests/
```

The submodule ships **code only** — the built SQLite databases live wherever you
ran `f1db backfill`. Point the backend at them via `F1DB_DATA_DIR` (see `.env.example`).

## Quickstart (Windows / PowerShell)

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
pip install -e .\external\f1-db          # the f1db data dependency
pip install -e ".[dev]"                   # f1_terminal + dev tools
Copy-Item .env.example .env               # then edit F1DB_DATA_DIR to your data dir

f1term serve                              # http://127.0.0.1:8000/docs
f1term repl                               # interactive console
pytest -q
```

## API (first feature)

| Endpoint | Purpose |
|---|---|
| `GET /sessions/{session_id}/laps?driver_id=` | raw lap times (for the React component) |
| `GET /sessions/{session_id}/stints` | per-stint tire summary |
| `GET /sessions/{session_id}/pit-stops` | pit stops |
| `GET /sessions/{session_id}/model-inputs/tire-deg?format=records\|columns` | clean lap+tire rows for the tire-deg model |
| `GET /seasons`, `/seasons/{y}/events`, `/seasons/{y}/drivers`, `/sessions?season=&round=` | catalogue |

Session IDs look like `2025_R10_R` (`{season}_R{round}_{code}`); driver IDs like
`max_verstappen_red_bull_2025`.
