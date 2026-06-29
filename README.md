# Aegis Concierge: Privacy-First Personal AI Assistant

## Problem Statement
Modern personal AI assistants lack transparent, proactive security measures to prevent data leakage (PII) and malicious prompt injections. They execute tasks without appropriate human authorization protocols.

## Solution Architecture
The Aegis Concierge solves this via a robust, 3-stage security pipeline leading into an intelligent multi-agent routing graph:

1. **PII Masking & Threat Scanning:** All input is immediately scrubbed for PII (SSN, Email, Phone, custom Policy IDs) using an isolated in-memory vault, while a Threat Scanner blocks injection vectors.
2. **Shadow-Mode Interceptor:** The sanitized prompt is scored heuristically for risky keywords to mandate Human-in-the-Loop (HITL) checks before routing.
3. **Cognitive Routing & Tool Execution (ADK/MCP):** The secure context is evaluated by a Router Node which delegates execution to specialized nodes (e.g., DeveloperNode for RAG context extraction).
4. **Audit Logging:** End-to-end cycle telemetry is persistently saved for compliance auditing.

### Competition Implementation Highlights
- **Concept 1: Multi-Agent System (ADK)** - Graph-based routing to specialized agent nodes (`skills/family_manager/routing_graph.py`).
- **Concept 2: Security Features** - PII Masking, Threat Scanning, and Audit Logging (`app.py`).
- **Concept 3: MCP Server** - Modular tool-calling architecture designed for local or remote integration (`tools/knowledge_tool.py`).

## Setup Instructions

1. **Install Dependencies:**
   Ensure you have Python 3.11+ installed.
   ```bash
   pip install -r requirements.txt
   ```
   *Note: This includes the `rich` library for the high-visibility Cyber-Security Control Center terminal UI.*

2. **Run the Application:**
   ```bash
   uvicorn app:app --reload
   ```

3. **Interact via API:**
   Use Swagger UI at `http://127.0.0.1:8000/docs` to POST requests to `/api/v1/chat`. Watch the terminal for interactive security intercepts!
