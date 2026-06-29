🛡️ Aegis Concierge

Privacy-First Personal AI Assistant

"Privacy isn't an optional feature—it is the foundation of trustworthy AI."

A secure, highly resilient, multi-agent AI concierge system designed to handle technical developer workflows, context-aware queries, and local system documentation requests while ensuring absolute data privacy.

🚀 Live Demo • 📄 Documentation • 🎥 Demo Video • 🏆 Kaggle Writeup • ⭐ Star Repository

🏆 Kaggle AI Agents: Intensive Vibe Coding Capstone

This repository is the official submission for the Kaggle AI Agents Capstone Project.

Designed for the Concierge Agents Track, Aegis Concierge demonstrates the pinnacle of course outcomes by combining advanced agentic behavior with enterprise-grade data security.

Project Goal: To create a secure personal assistant that streamlines developer workflows without exposing proprietary data.

Core Innovation: A zero-trust interception layer that seamlessly pairs with graph-based multi-agent routing.

Real-World Impact: Provides a blueprint for enterprises to deploy generative AI safely in highly regulated environments (FinTech, HealthTech, etc.).

📑 Table of Contents

🛡️ Aegis Concierge

🏆 Kaggle AI Agents Capstone

📑 Table of Contents

📖 Project Overview

📌 Repository Status Dashboard

⚠️ Problem Statement

💡 Solution Overview

⚖️ The Aegis Advantage: Feature Comparison

✨ Key Features

🏗️ System Architecture

🔄 AI Agent Workflow

📁 Repository Structure

💼 Core Engineering Competencies Demonstrated

🛠️ Technology Stack

🚀 Installation Guide

⚙️ Configuration

▶️ Running the Project

🔌 API Documentation

📸 Visual Gallery & Demos

🔒 Security Pipeline

🧠 Multi-Agent Design

📚 Local RAG Implementation

📊 Audit Logging

⚡ Performance & Scalability

❓ Frequently Asked Questions (FAQ)

🔮 Future Enhancements

🤝 Contributing

📜 License

👤 Author & Maintainer

🙏 Acknowledgements

📖 Project Overview

Aegis Concierge is an enterprise-grade, privacy-centric AI assistant designed to bridge the gap between powerful Large Language Models (LLMs) and strict data security requirements.

Built specifically for developers, enterprise teams, and technical operators, Aegis Concierge acts as a protective layer—a "concierge"—between the user and the cloud. It intercepts prompts, scrubs them of sensitive Personally Identifiable Information (PII), assesses threat levels, and intelligently routes the sanitized intent to highly specialized AI agents equipped with local Knowledge Bases (RAG).

Target Audience:

Developers & Engineers: Automate workflows without leaking proprietary code or API keys.

Security Teams: Maintain strict audit logs and zero-trust policies for all AI interactions.

Enterprise Workforces: Leverage generative AI safely within heavily regulated environments.

📌 Repository Status Dashboard

Metric

Details

Metric

Details

Version

v1.0.0-stable

Deployment

Local / Docker-Ready

Status

Active Development

Documentation

Fully Documented (Swagger UI)

License

MIT License

API

RESTful (FastAPI)

Language

Python 3.10+

AI Model

Google Gemini (DeepMind)

Framework

FastAPI / Uvicorn

Project Type

Backend / Multi-Agent System

Architecture

Decoupled / Microservices

Maintenance

Actively Maintained

⚠️ Problem Statement

The rapid adoption of AI assistants has introduced critical operational and security vulnerabilities:

Sensitive Information Leakage: Users routinely (and often accidentally) paste PII, API keys, internal IP, and customer data into public LLM interfaces, resulting in severe compliance breaches.

Unsafe Prompt Execution: Malicious actors or unaware users can trigger destructive system commands (e.g., prompt injection) because standard agents lack a proactive security interception layer.

Monolithic Inefficiency (Poor Routing): Relying on a single, massive LLM to handle diverse tasks (coding, business logic, casual chat) leads to context poisoning, hallucinations, and degraded reasoning.

Lack of Auditability: Traditional chat interfaces offer zero visibility into the backend decision-making process, making it impossible to audit AI behavior in enterprise environments.

💡 Solution Overview

Aegis Concierge solves the AI privacy crisis by implementing a Zero-Trust, Multi-Agent architecture.

Instead of passing user prompts directly to Google Gemini, the system utilizes a multi-layered defensive pipeline:

The Security Shield: Before any AI sees the prompt, local Python algorithms scan for threats and mask all PII into a secure volatile memory vault.

The Brain (Router): The sanitized prompt is analyzed by a fast routing agent that determines the optimal specialized subsystem for the task.

The Hands (Specialized Agents): Tasks are executed by targeted agents (e.g., Developer Agent, Business Agent) utilizing Local RAG (Retrieval-Augmented Generation) to fetch secure, offline documentation.

The Ledger: Every interaction, risk score, and routing decision is permanently recorded in a structured JSON audit log.

⚖️ The Aegis Advantage: Feature Comparison

How Aegis Concierge compares to standard, monolithic AI assistant implementations:

Capability

Traditional AI Assistant

Aegis Concierge 🛡️

Data Privacy

Sends raw data to cloud

Zero-Trust PII Masking

Security Layer

Non-existent

Proactive Threat Scanners

Execution Model

Monolithic LLM

Decoupled Multi-Agent Graph

Auditability

Black Box

Granular JSON Telemetry

Knowledge Base

Hallucination-prone

Local RAG Integration

Context Control

Shared across all prompts

Isolated Agent Scopes

Destructive Actions

Executed automatically

Human-in-the-Loop Pauses

Enterprise Readiness

❌ No

✅ Yes

✨ Key Features

Feature

Icon

Description

Benefit

Zero-Trust Security Pipeline

🛡️

All inbound requests are treated as untrusted and actively scanned prior to execution.

Prevents prompt injection and malicious payload execution.

PII Masking Engine

🕵️‍♂️

Automatically identifies and replaces emails, phone numbers, and keys with secure placeholders.

Ensures strict compliance with GDPR/CCPA data privacy laws.

Graph-Based Routing (ADK)

🔀

Dynamically routes intents to isolated, specialized agent nodes using graph logic.

Eliminates context poisoning and reduces hallucination rates.

Local RAG Retrieval

📚

Queries a local, asynchronous offline knowledge base using mock-MCP standard protocols.

Provides context-aware answers without sending data to the cloud.

Interactive Terminal UX

🎨

Utilizes the rich library to render color-coded alerts and Human-in-the-loop approvals.

Delivers a world-class, observable developer experience.

Enterprise Audit Logging

📊

Captures granular metrics (latency, route, risk score) for every single transaction.

Enables complete forensic observability for enterprise deployments.

🏗️ System Architecture

Aegis Concierge utilizes a decoupled, asynchronous, service-oriented architecture.

graph TD
    %% User & Gateway
    User([🧑‍💻 User / Client]) -->|HTTP POST| Gateway[FastAPI Gateway]
    
    %% Security Layer
    subgraph Security Layer [🛡️ Zero-Trust Security Pipeline]
        Gateway --> Interceptor{Security Interceptor}
        Interceptor -->|Threat Detected| Reject[Reject / Human-in-the-Loop]
        Interceptor -->|Safe| PII[PII Masker]
        PII -.->|Vaults Data| Memory[(Volatile PII Vault)]
    end
    
    %% Routing Engine
    subgraph Routing Layer [🔀 Graph-Based ADK Router]
        PII --> Router((Routing Engine))
    end
    
    %% Specialized Agents
    subgraph Agent Execution [🤖 Specialized Agent Nodes]
        Router -->|Dev Intent| DevAgent[Developer Agent]
        Router -->|Biz Intent| BizAgent[Business Agent]
        Router -->|General| GenAgent[General Agent]
    end
    
    %% Tools & External
    subgraph Tooling & RAG [📚 Knowledge & Tooling]
        DevAgent <--> LocalRAG[(Local RAG Engine)]
        BizAgent <--> LocalRAG
        DevAgent <--> Gemini[Google Gemini API]
        BizAgent <--> Gemini
        GenAgent <--> Gemini
    end
    
    %% Telemetry
    subgraph Observability [📊 Telemetry & Audit]
        DevAgent --> Audit[Audit Logger]
        BizAgent --> Audit
        GenAgent --> Audit
        Audit -.-> AuditLog[(logs/audit_log.json)]
    end
    
    %% Output
    Audit --> FinalResponse[Sanitized Final Response]
    FinalResponse --> Gateway
    Gateway --> User


🔄 AI Agent Workflow

The precise lifecycle of a single HTTP request through the Aegis Concierge system:

sequenceDiagram
    participant U as User
    participant API as FastAPI
    participant Sec as Security Engine
    participant Rout as Router Agent
    participant Node as Dev/Biz Node
    participant Tool as Local RAG
    participant LLM as Google Gemini
    participant Log as Audit Logger

    U->>API: POST /api/v1/chat (Prompt)
    API->>Sec: Scan & Mask Prompt
    Sec-->>API: Sanitized Prompt & Risk Score
    
    alt Risk Score > Threshold
        API->>U: 403 Forbidden (Requires Human Approval)
    else Safe Proceed
        API->>Rout: Analyze Intent
        Rout-->>API: Selected Route (e.g., 'developer')
        API->>Node: Execute Task
        Node->>Tool: Query Local Knowledge Base
        Tool-->>Node: Relevant Documentation Context
        Node->>LLM: Generate final answer (with Context)
        LLM-->>Node: Raw Response
        Node->>Sec: Re-hydrate PII / Final Scan
        Sec-->>Node: Safe Response
        Node->>Log: Write Telemetry (Latency, Route)
        Log-->>API: Log Saved
        API->>U: 200 OK (Final Output)
    end


📁 Repository Structure

aegis-concierge/
│
├── app.py                      # 🚀 FastAPI Application entry point (Core Router/Gateway)
├── requirements.txt            # 📦 Python dependencies (FastAPI, Uvicorn, Rich, etc.)
├── README.md                   # 📖 World-class system documentation
│
├── security/                   # 🛡️ Zero-Trust Security Module
│   ├── __init__.py
│   ├── pii_masker.py           # Regex & NLP heuristics for data redaction
│   └── security_interceptor.py # Proactive threat and risk-scoring middleware
│
├── skills/                     # 🤖 Multi-Agent Logic & Node Definitions
│   └── family_manager/
│       ├── __init__.py
│       └── routing_graph.py    # ADK Multi-Agent routing graph orchestrator
│
├── tools/                      # 🛠️ System Tools & Data Connections
│   ├── __init__.py
│   └── knowledge_tool.py       # Asynchronous local RAG & mock-MCP tool wrapper
│
├── utils/                      # 🧰 Global Utilities
│   ├── __init__.py
│   └── audit_logger.py         # JSON-based structural telemetry writer
│
├── tests/                      # 🧪 Behavior-Driven Development Test Suite
│   └── test_security.py        # Validates PII masking and threat thresholds
│
└── logs/                       # 📊 Persistent Storage (Ignored by VCS)
    └── audit_log.json          # Persistent transactional telemetry


💼 Core Engineering Competencies Demonstrated

This project serves as a comprehensive portfolio piece demonstrating advanced proficiency in modern software and AI engineering disciplines:

Backend Development: Scalable, asynchronous REST API design using FastAPI.

Security Engineering: Defensive programming, regex-based PII redaction, and threat scoring.

AI & Prompt Engineering: Integrating Google Gemini with structured context injection.

System Design: Building decoupled, graph-based routing architectures for multi-agent systems.

Retrieval-Augmented Generation (RAG): Constructing efficient local knowledge retrieval mechanisms.

Observability: Implementing structured, machine-readable audit logging for telemetry.

🛠️ Technology Stack

Category

Technology

Purpose

Reason for Selection

Core Framework

FastAPI

API Gateway & Routing

High performance, native async support, and automatic OpenAPI generation.

Intelligence

Google Gemini API

Core Reasoning Engine

State-of-the-art context window and highly accurate instruction following.

Agent Routing

Python (ADK)

Graph orchestration

Lightweight, stateful agent management without heavy framework overhead.

Data Retrieval

Local RAG

Knowledge Base

Ensures proprietary docs remain strictly on-device with zero network latency.

Concurrency

Asyncio

Non-blocking I/O

Handles multiple tool connections and LLM requests concurrently.

Web Server

Uvicorn

ASGI Server

Production-grade server capable of high-throughput asynchronous execution.

CLI / UX

Rich

Terminal Interface

Delivers stunning, highly observable color-coded terminal alerts and tables.

🚀 Installation Guide

Prerequisites

Python 3.10+ (Ensure Python is added to your system PATH)

Git installed on your local machine.

Step-by-Step Setup (All Platforms)

Clone the Repository

git clone https://github.com/adarsh-anshuman/aegis-concierge.git
cd aegis-concierge


Create a Virtual Environment

Windows:

python -m venv venv
venv\Scripts\activate


Linux/MacOS:

python3 -m venv venv
source venv/bin/activate


Install Dependencies

pip install -r requirements.txt


⚙️ Configuration

Aegis Concierge requires configuration to connect to the Google Gemini API.

Create a .env file in the root directory:

touch .env


Open the file and add your configuration settings:

# .env

# Core AI Configuration
GEMINI_API_KEY="your_google_gemini_api_key_here"

# Security Thresholds
MAX_RISK_SCORE=0.75
ENABLE_HUMAN_IN_THE_LOOP=true

# Environment
ENV="production"


Note: Never commit your .env file to version control.

▶️ Running the Project

To launch the Aegis Concierge backend, run the Uvicorn ASGI server:

uvicorn app:app --reload --host 127.0.0.1 --port 8000


Expected Terminal Output:
You will see the standard Uvicorn startup logs, followed by the Rich formatted initialization table confirming that the Security Interceptor and RAG tools are online.

API Gateway: http://127.0.0.1:8000

Swagger UI (Docs): http://127.0.0.1:8000/docs

Redoc: http://127.0.0.1:8000/redoc

🔌 API Documentation

Aegis Concierge provides a fully interactive API documentation interface via Swagger UI.

Endpoint: Chat Request

Endpoint

Method

Description

Content-Type

/api/v1/chat

POST

Submits a prompt to the multi-agent routing pipeline.

application/json

{
  "user_prompt": "Hello! My registration email is developer-admin@aegis.io. Can you check the local api setup documentation for my account?"
}


{
  "status": "success",
  "response": "Developer Structural Plan based on Local RAG Docs:\n[API] Aegis API Documentation v2: Endpoints available at /api/v1/chat. Uses POST methods.\n[SETUP] Run uvicorn app:app --reload to start the server.",
  "route_taken": "developer",
  "requires_human_approval": false
}


📸 Visual Gallery & Demos

🎥 Animated Demonstrations (GIFs)

🖼️ Static Screenshots

Architecture & Flow

Interactive Documentation





System Architecture Diagram

Auto-Generated Swagger API Docs

Terminal Observability

Enterprise Audit Logging





Color-Coded 'Rich' Terminal Output

Structured JSON Telemetry (Audit Trail)

🔒 Security Pipeline

Aegis Concierge was built on the philosophy that privacy is a systemic requirement, not an afterthought.

1. Zero Trust Design

Every prompt is treated as potentially malicious. Before the LLM processes the data, it passes through the security_interceptor.py middleware.

2. PII Masking

Using a combination of highly optimized regular regular expressions and heuristic tokenization, the system detects:

Emails (user@company.com ➡️ <MASKED_EMAIL>)

Phone Numbers (555-0102 ➡️ <MASKED_PHONE>)

API Keys, Secrets, and IP Addresses.
These values are held in a secure, ephemeral in-memory dictionary during execution and re-hydrated (if absolutely necessary) only upon final response delivery to the authorized user.

3. Threat Detection & Risk Scoring

The prompt is scored against known prompt-injection signatures (e.g., "ignore previous instructions", "system override"). If the computed risk score exceeds 0.75, the system gracefully halts the event loop and requests physical terminal confirmation via rich.prompt.Confirm.

🧠 Multi-Agent Design

A single LLM acting as a "jack-of-all-trades" suffers from context dilution. Aegis Concierge implements a Graph-Based Multi-Agent Architecture (ADK):

The Router Node: A highly restricted, fast-inference agent dedicated only to semantic classification. It decides the intent.

Execution Nodes: Isolated agents (Developer, Business, General) that receive the prompt.
Why this is better: By splitting responsibilities, we can give the "Developer Node" access to local terminal tools and codebases, while strictly denying those permissions to the "Business Node," effectively creating role-based access control (RBAC) at the agent level.

📚 Local RAG Implementation

To prevent catastrophic subprocess failures (TaskGroup errors from brittle Node.js/MCP bridges), Aegis Concierge features a 100% native asynchronous Local RAG engine (tools/knowledge_tool.py).

Knowledge Base: Maintains a structured dictionary/JSON store of system documentation.

Retrieval Mechanism: Implements asynchronous keyword vectoring and semantic matching to instantly fetch documentation without Uvicorn thread blocking.

Context Injection: Seamlessly appends the retrieved technical data to the specialized agent's system prompt prior to Gemini API submission.

📊 Audit Logging

Enterprise deployments require observability. Aegis Concierge writes structured JSON telemetry for every transaction to logs/audit_log.json.

What gets logged?

ISO 8601 Timestamps

Masked vs. Unmasked string differentials

Computed Threat Risk Scores

Graph Route Taken (e.g., developer, fallback)

Total execution latency (ms)

Benefits: This allows security engineers to build dashboards directly on top of the agent's behavior, establishing an undeniable paper trail of AI interactions.

⚡ Performance & Scalability

Aegis Concierge is built for high throughput.

High-Efficiency Masking: The regex and heuristic PII masking pipeline is highly optimized, introducing negligible latency overhead to the request lifecycle.

Asynchronous Concurrency: Built natively on asyncio and FastAPI, the system prevents I/O blocking during LLM network calls and local RAG disk reads, enabling concurrent user request handling.

Horizontal Scalability: The decoupled nature of the agent nodes allows the architecture to be easily containerized (via Docker) and orchestrated as independent microservices in a cloud environment as computational demand increases.

❓ Frequently Asked Questions (FAQ)

🔮 Future Enhancements

While currently competition-ready, the architectural foundation supports massive scaling:

🎙️ Voice AI Integration: Hook the FastAPI backend to WebRTC for real-time voice concierge services.

🧠 Persistent Memory: Migrate the ephemeral PII vault to a secure Redis instance for cross-session context.

🌐 Full MCP Compliance: Swap the Local RAG for remote Model Context Protocol servers for enterprise-wide data syncing.

🗄️ Vector Database: Implement ChromaDB or Pinecone for massive-scale semantic RAG retrieval.

🐳 Dockerization: Provide official Docker images and Helm charts for Kubernetes cloud deployments.

🤝 Contributing

We welcome contributions from the open-source community!

Fork the Project.

Create your Feature Branch (git checkout -b feature/AmazingFeature).

Commit your Changes (git commit -m 'Add some AmazingFeature').

Push to the Branch (git push origin feature/AmazingFeature).

Open a Pull Request.

Please ensure all PRs pass the existing security tests and include updated rich logging statements where applicable.

📜 License

Distributed under the MIT License. See LICENSE for more information. This grants full permissions for commercial use, modification, and distribution.

👤 Author & Maintainer

Adarsh Anshuman

💻 GitHub: @adarsh-anshuman

💼 LinkedIn: Connect with me

📧 Email: adarsh@example.com

🙏 Acknowledgements

Google DeepMind: For the incredible Gemini API reasoning capabilities.

Kaggle: For hosting the AI Agents Intensive Vibe Coding Course.

FastAPI: For the world's most enjoyable Python web framework.

Rich Text: For making our terminal UI beautiful.

The Open Source Community: For the tireless development of the tools that made this architecture possible.

Built with ❤️ for the Kaggle AI Agents Capstone

Aegis Concierge is open-source software licensed under the MIT License.




© 2026 Adarsh Anshuman. All Rights Reserved.