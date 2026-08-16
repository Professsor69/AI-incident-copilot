"""
Reflexion / Critic Node — Phase 5.4

Before returning the final answer, passes the agent's draft diagnosis to
a separate prompt: "Does the retrieved data actually prove this hypothesis?"

If evidence is insufficient or the agent has hallucinated, this node sends
the loop back to collect more data.
"""

# TODO: Implement in Phase 5


async def critique_diagnosis(draft: str, evidence: list[dict]) -> tuple[bool, str]:  # type: ignore[type-arg]
    """Validate a draft diagnosis against the collected evidence.

    Args:
        draft: The agent's preliminary diagnosis string.
        evidence: List of evidence dicts collected by the executor.

    Returns:
        A tuple of (is_grounded: bool, feedback: str).
        If is_grounded is False, the feedback explains what's missing.
    """
    # Placeholder — always approves until Phase 5 implementation
    return True, "Diagnosis approved (placeholder — implement in Phase 5)"
