"""
Pydantic Tool Schemas — Phase 4.1

Strict schemas for all LLM-callable tools. The LLM uses these to understand
exactly what arguments to provide when making tool calls.
"""

from pydantic import BaseModel, Field


class QueryLogsInput(BaseModel):
    """Input schema for the query_logs tool."""

    service_name: str = Field(
        ...,
        description="Name of the service to query logs for (e.g., 'checkout', 'payment').",
        examples=["checkout", "auth", "payment"],
    )
    time_window_minutes: int = Field(
        default=30,
        ge=1,
        le=1440,
        description="Time window in minutes to look back from now (max 1440 = 24h).",
    )


class GetSystemMetricsInput(BaseModel):
    """Input schema for the get_system_metrics tool."""

    service_name: str = Field(
        ...,
        description="Name of the service to retrieve CPU and memory metrics for.",
        examples=["checkout", "redis", "postgres"],
    )


class CheckDeployHistoryInput(BaseModel):
    """Input schema for the check_deploy_history tool."""

    since_minutes: int = Field(
        default=60,
        ge=1,
        le=1440,
        description="How many minutes back to check for deployments.",
    )


class SearchRunbooksInput(BaseModel):
    """Input schema for the search_runbooks tool."""

    query: str = Field(
        ...,
        description=(
            "Natural language or keyword query to search the runbook knowledge base. "
            "Include error codes, symptoms, and service names for best results."
        ),
        examples=[
            "Redis connection pool exhaustion 503 errors",
            "memory leak Python GC pressure",
            "Postgres slow queries N+1",
        ],
    )
    top_k: int = Field(
        default=3,
        ge=1,
        le=10,
        description="Number of top runbook chunks to return.",
    )


class ToolCallResult(BaseModel):
    """Standard result wrapper returned by all tool calls."""

    tool_name: str
    success: bool
    data: dict  # type: ignore[type-arg]
    error: str | None = None
    latency_ms: float = 0.0
