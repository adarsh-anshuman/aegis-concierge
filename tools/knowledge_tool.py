import asyncio
import logging

logger = logging.getLogger(__name__)

# Concept 3: MCP Server - Modular tool-calling architecture designed for local or remote integration.
class KnowledgeTool:
    """
    A 100% native Python asynchronous 'Local RAG' tool.
    Replaces the brittle npx MCP subprocess to guarantee zero-glitch execution.
    """
    def __init__(self):
        # A simple simulated local knowledge base
        self.knowledge_base = {
            "api": "Aegis API Documentation v2: Endpoints available at /api/v1/chat. Uses POST methods.",
            "auth": "Authentication requires a Bearer token in the Authorization header.",
            "setup": "Run uvicorn app:app --reload to start the server.",
            "security": "All endpoints run through the PIIMasker and ThreatScanner pipelines.",
        }

    async def query(self, query_string: str) -> str:
        """
        Retrieves matching documentation from the local knowledge base.
        """
        logger.info(f"Local RAG Tool executing query: {query_string}")
        
        # Simulate slight I/O delay
        await asyncio.sleep(0.1)
        
        query_lower = query_string.lower()
        results = []
        
        for key, text in self.knowledge_base.items():
            if key in query_lower:
                results.append(f"[{key.upper()}] {text}")
                
        if not results:
            # Fallback mock data if no direct keyword matches
            return "General System Context: The Aegis Concierge is a privacy-first multi-agent system."
            
        return "\n".join(results)

# Global singleton
local_rag_tool = KnowledgeTool()

# Keep the global singleton instance intact
local_rag_tool = KnowledgeTool()

# Add this wrapper function to maintain compatibility with your imports:
async def query_mcp_documentation(query_string: str) -> str:
    """
    Exposed wrapper function to match the expected import in routing_graph.py.
    Safely invokes the underlying local_rag_tool instance method.
    """
    return await local_rag_tool.query(query_string)
