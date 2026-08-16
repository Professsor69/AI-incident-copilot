"""
Markdown Chunker — Phase 3.1

Parses runbook Markdown files and splits them by header (##) rather than
by arbitrary character counts. This preserves semantic coherence in chunks
and ensures each chunk has meaningful context.
"""

from pathlib import Path

# TODO: Implement full chunker in Phase 3


def chunk_markdown_by_headers(filepath: Path) -> list[dict[str, str]]:
    """Parse a Markdown file and return chunks split by ## headers.

    Args:
        filepath: Path to the .md runbook file.

    Returns:
        List of dicts with keys: 'source', 'header', 'content', 'chunk_id'.
    """
    # Placeholder
    return []


def load_all_runbooks(runbooks_dir: Path) -> list[dict[str, str]]:
    """Load and chunk all .md files in a directory.

    Args:
        runbooks_dir: Path to the directory containing runbook .md files.

    Returns:
        Combined list of all chunks from all runbooks.
    """
    all_chunks: list[dict[str, str]] = []
    for md_file in runbooks_dir.glob("*.md"):
        chunks = chunk_markdown_by_headers(md_file)
        all_chunks.extend(chunks)
    return all_chunks
