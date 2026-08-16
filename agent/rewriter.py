"""
Query Rewriter — Phase 5.1

Rewrites vague user queries into formal diagnostic queries before
passing them to the RAG pipeline or agent planning stage.

Example:
    Input:  "Checkout is slow"
    Output: "Elevated latency on checkout service — investigate error rates,
             resource utilization, and recent code deployments."
"""

# TODO: Implement in Phase 5


async def rewrite_query(raw_query: str) -> str:
    """Rewrite a vague incident description into a structured diagnostic query.

    Args:
        raw_query: The raw user-provided incident description.

    Returns:
        A formal, structured query suitable for the agent planner.
    """
    # Placeholder — returns the original query until Phase 5 implementation
    return raw_query
