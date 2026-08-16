"""
Multi-Step Planner — Phase 5.2

Forces the LLM to output a JSON array of diagnostic steps before execution,
preventing erratic tool selection in a naive ReAct loop.

Example output:
    [
        "1. Query checkout api_logs from 13:50 to 14:10",
        "2. Retrieve CPU and memory metrics for checkout service",
        "3. Check deploy history between 13:45 and 14:05",
        "4. Search runbooks for 503 errors and connection pool exhaustion"
    ]
"""

# TODO: Implement in Phase 5


async def generate_plan(diagnostic_query: str) -> list[str]:
    """Generate a structured diagnostic plan from a formal query.

    Args:
        diagnostic_query: A rewritten, formal incident query.

    Returns:
        A list of ordered investigation steps.
    """
    # Placeholder
    return [f"1. Investigate: {diagnostic_query}"]
