"""
BM25 Sparse Index — Phase 3.3

Builds and queries a BM25 index over runbook chunks using rank-bm25.
BM25 catches exact error codes (ERR_CONN_503, OOM_KILLER) that vector
search misses due to poor embedding coverage of rare tokens.
"""

# TODO: Implement in Phase 3


class BM25Index:
    """BM25 sparse retrieval index over runbook chunks."""

    def __init__(self) -> None:
        self._index = None
        self._chunks: list[dict[str, str]] = []

    def build(self, chunks: list[dict[str, str]]) -> None:
        """Build the BM25 index from a list of text chunks.

        Args:
            chunks: List of chunk dicts (must have 'content' key).
        """
        # TODO: Implement with rank-bm25 in Phase 3
        self._chunks = chunks

    def search(self, query: str, top_k: int = 15) -> list[tuple[int, float]]:
        """Search the BM25 index.

        Args:
            query: Search query string.
            top_k: Number of top results to return.

        Returns:
            List of (chunk_index, score) tuples sorted by score descending.
        """
        # Placeholder
        return []
