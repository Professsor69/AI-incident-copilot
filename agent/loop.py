"""
Main Agentic Reasoning Loop — Phase 5

Orchestrates the full Plan-and-Solve pipeline:
    1. Query Rewriter   (Phase 5.1)
    2. Multi-Step Planner (Phase 5.2)
    3. Execution Node   (Phase 5.3)
    4. Reflexion/Critic (Phase 5.4)
    5. Final Response

Yields streaming events for SSE consumption (Phase 8).
"""

from collections.abc import AsyncIterator

# TODO: Wire up all nodes in Phase 5


async def run_diagnostic_loop(raw_query: str) -> AsyncIterator[str]:
    """Run the full agentic diagnostic loop, yielding streaming status events.

    Args:
        raw_query: The raw user-provided incident description.

    Yields:
        Status strings for SSE streaming (e.g., "Rewriting query...",
        "Querying logs...", "Final diagnosis: ...")
    """
    yield f"[INFO] Received query: {raw_query}"
    yield "[INFO] Agent loop not yet implemented — coming in Phase 5"
