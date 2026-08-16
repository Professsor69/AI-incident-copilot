# System Design: AI Incident Copilot

**Author:** Professsor69  
**Date:** August 2026  
**Status:** Active Development

---

## Problem Statement

When a production incident occurs, engineers must manually correlate data from logs, metrics dashboards, deploy history, and internal runbooks — a process that can take 15–60 minutes. The AI Incident Copilot automates this diagnostic workflow using an LLM agent with structured reasoning and a production-grade retrieval system.

---

## System Components

```
┌─────────────────────────────────────────────────────────────────────┐
│                        CLIENT (HTTP / SSE)                          │
└──────────────────────────────┬──────────────────────────────────────┘
                               │ POST /diagnose
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     API LAYER (FastAPI)                             │
│  • /diagnose endpoint          • SSE streaming                      │
│  • Redis rate limiter          • Redis response cache (5-min TTL)   │
└──────────────────────────────┬──────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    AGENT ORCHESTRATOR (LLM)                         │
│  ┌────────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────────┐  │
│  │  Query     │→ │ Planner  │→ │ Executor │→ │ Critic / Reflex  │  │
│  │  Rewriter  │  │(JSON plan│  │(tool loop│  │(hallucination    │  │
│  │            │  │  array)  │  │)         │  │ guard)           │  │
│  └────────────┘  └──────────┘  └──────────┘  └──────────────────┘  │
└───────────────────────────────┬─────────────────────────────────────┘
                                │ tool calls
            ┌───────────────────┼─────────────────────┐
            ▼                   ▼                     ▼
┌──────────────────┐  ┌──────────────────┐  ┌────────────────────────┐
│   DATA TOOLS     │  │   RAG PIPELINE   │  │  MOCK DEPLOY API       │
│                  │  │                  │  │                        │
│ query_logs()     │  │ ChromaDB (dense) │  │ mock_deploys.json      │
│   → SQLite       │  │ + BM25 (sparse)  │  │ (simulated GitHub PRs) │
│   api_logs       │  │ + RRF fusion     │  └────────────────────────┘
│                  │  │ + Cross-encoder  │
│ get_system_      │  │   reranker       │
│ metrics()        │  │                  │
│   → SQLite       │  │ → Top-3 Runbook  │
│   system_metrics │  │   Chunks         │
└──────────────────┘  └──────────────────┘
            │
            ▼
┌─────────────────────────────────────────────────────────────────────┐
│                 OBSERVABILITY (Langfuse)                             │
│  • Per-request traces            • Token count + cost tracking       │
│  • Tool call latencies           • RAG chunk audit log               │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Component Summary

| Component | Technology | Role |
|-----------|-----------|------|
| **API** | FastAPI + uvicorn | HTTP interface, SSE streaming, request routing |
| **Rate Limiter / Cache** | Redis | Sliding-window rate limiting, 5-min response cache |
| **LLM Orchestrator** | Gemini 2.5 Flash | Query rewriting, planning, execution, critique |
| **Eval Judge** | GPT-4o-mini | Independent grading of agent outputs |
| **Vector DB** | ChromaDB | Dense semantic search over runbook chunks |
| **Keyword Search** | rank-bm25 | Sparse exact-match search over runbook chunks |
| **Fusion** | RRF (custom impl.) | Merges dense + sparse results mathematically |
| **Reranker** | BAAI/bge-reranker-base | Cross-encoder final scoring of top-15 → top-3 |
| **Relational DB** | SQLite | Simulated telemetry (api_logs, system_metrics) |
| **Knowledge Base** | 20 Markdown runbooks | Structured incident investigation guides |
| **Observability** | Langfuse | Full trace logging, token cost tracking |

---

## Data Flow: Incident Diagnosis Request

1. **Ingress** — User POSTs `{"query": "Checkout is slow since 14:00"}` to `/diagnose`
2. **Cache Check** — Redis checks if an identical query was answered < 5 minutes ago
3. **Query Rewriting** — Cheap LLM call: `"Checkout is slow"` → `"Elevated latency on checkout service after 14:00, investigate error rates, resource utilization, and recent deployments"`
4. **Planning** — LLM emits JSON plan: `["1. Query checkout api_logs 13:50-14:10", "2. Get checkout CPU/memory metrics", "3. Check deploy history 13:45-14:05", "4. Search runbooks for latency + 503"]`
5. **Execution** — Agent executes each step via tool calls, aggregating evidence
6. **Critique** — Second LLM prompt validates: "Does the evidence actually support this hypothesis?"
7. **Response** — Grounded, evidence-backed diagnosis streamed via SSE

---

## Key Design Decisions

- **Hybrid RAG over pure vector search**: Error codes like `ERR_CONN_503` have no semantic neighbors; BM25 catches exact tokens that embeddings miss.
- **Plan-and-Solve over ReAct**: Structured planning prevents erratic tool selection; the critic prevents hallucination.
- **Cross-encoder reranker**: Embedding similarity ≠ relevance; the reranker scores the query-chunk relationship directly.
- **Different models for agent vs. judge**: Eliminates self-grading bias in the evaluation harness.
- **SSE streaming**: Users see agent reasoning in real-time instead of waiting 15+ seconds for a result.

---

## Scalability Notes

- **Horizontal scaling**: FastAPI is stateless; Redis handles shared cache/rate-limit state across instances.
- **ChromaDB**: Can be swapped for Pinecone or Weaviate for cloud-scale vector search.
- **SQLite → Postgres**: The data layer abstracts behind a repository pattern; SQLite is a mock for the real telemetry store.
