import traceback
import logging
import sys
from pathlib import Path

# Add project root to path for absolute imports
project_root = Path(__file__).parent.parent
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

from tools.knowledge_tool import local_rag_tool

logger = logging.getLogger(__name__)

async def query_mcp_documentation(query: str) -> str:
    """
    Asynchronous entrypoint to pass text queries to the documentation engine.
    Refactored to use the native Local RAG tool for 100% zero-glitch stability,
    replacing the brittle Node.js MCP subprocess.
    """
    try:
        return await local_rag_tool.query(query)
    except Exception as e:
        logger.error(f"Critical error in native documentation retrieval: {e}")
        # Never swallow errors silently.
        raise
