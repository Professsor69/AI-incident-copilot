"""
FastAPI application entry point.

Phase 8 will add: SSE streaming, Redis cache middleware, rate limiting.
This module wires together all routes and middleware.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.config import settings

app = FastAPI(
    title="AI Incident Copilot",
    description=(
        "Production-grade AI agent for autonomous incident diagnosis "
        "using Hybrid RAG and structured agentic reasoning."
    ),
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS — restrict in production
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"] if settings.is_development else [],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", tags=["health"])
async def health_check() -> dict[str, str]:
    """Liveness check endpoint."""
    return {"status": "ok", "env": settings.app_env}


# Routes are registered here as phases progress:
# Phase 8: from api.routes.diagnose import router
# app.include_router(router, prefix="/api/v1")
