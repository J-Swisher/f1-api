"""FastAPI application factory.

Importing this module imports the ``f1_terminal`` package first, which configures
the ``F1DB_*`` environment before any ``f1db`` import happens (see the package
``__init__``).
"""
from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from f1_terminal.api.routers import (
    catalogue,
    drivers,
    laps,
    results,
    session_summary,
    stints,
)
from f1_terminal.config import settings
from f1_terminal.db.engine import init_app_db


def create_app() -> FastAPI:
    app = FastAPI(
        title="F1 Terminal API",
        version="0.1.0",
        summary="Lap-time & tire-data service for the F1 terminal.",
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins_list,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/health", tags=["meta"])
    def health() -> dict:
        return {"status": "ok"}

    app.include_router(catalogue.router)
    app.include_router(drivers.router)
    app.include_router(laps.router)
    app.include_router(results.router)
    app.include_router(session_summary.router)
    app.include_router(stints.router)

    init_app_db()  # create the app DB + tables (idempotent)
    return app


app = create_app()
