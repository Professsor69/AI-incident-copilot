"""
Cross-Encoder Reranker — Phase 3.5

Takes the Top-15 RRF results and reranks them using BAAI/bge-reranker-base.
Unlike bi-encoder embeddings, a cross-encoder scores the exact query–chunk
pair jointly, producing much higher precision for the final Top-3.
"""

# TODO: Implement in Phase 3


class CrossEncoderReranker:
    """Cross-encoder reranker using BAAI/bge-reranker-base."""

    MODEL_NAME = "BAAI/bge-reranker-base"

    def __init__(self) -> None:
        self._model = None

    def load(self) -> None:
        """Load the cross-encoder model. Call once at startup."""
        # TODO: Load with sentence-transformers CrossEncoder in Phase 3
        pass

    def rerank(
        self,
        query: str,
        candidates: list[dict[str, float]],
        top_k: int = 3,
    ) -> list[dict[str, float]]:
        """Rerank candidate chunks by exact query-chunk relevance.

        Args:
            query: The diagnostic query string.
            candidates: Top-15 chunks from RRF (with 'content' key).
            top_k: Number of final results to return.

        Returns:
            Top-k chunks sorted by cross-encoder score descending.
        """
        # Placeholder
        return candidates[:top_k]
