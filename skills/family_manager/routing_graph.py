import sys
import asyncio
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.prompt import Confirm
from rich.panel import Panel

# Add the project root to the path
project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

from tools.knowledge_tool import query_mcp_documentation

# Concept 1: Multi-Agent System (ADK) - Graph-based routing to specialized agent nodes.
console = Console()

class RoutingGraph:
    """
    Standard asynchronous Python implementation of a multi-agent routing graph
    and orchestration pipeline with Rich terminal UI integration.
    """

    def __init__(self):
        self.dev_keywords = ["tool", "documentation", "api", "code", "generate", "script", "mcp"]
        self.mutation_keywords = ["write", "create", "modify", "delete", "update", "save", "remove", "book", "buy"]

    def _is_mutation_task(self, prompt: str) -> bool:
        return any(kw in prompt for kw in self.mutation_keywords)

    async def _router_node(self, ctx: dict) -> dict:
        prompt = ctx.get("masked_prompt", "").lower()
        
        # Calculate a basic confidence score for the UI
        dev_matches = sum(1 for kw in self.dev_keywords if kw in prompt)
        confidence = min(100, 50 + (dev_matches * 15))
        
        if dev_matches > 0:
            ctx["route"] = "developer"
        else:
            ctx["route"] = "task_execution"
            confidence = 85 # Default high confidence for basic tasks
            
        ctx["confidence"] = confidence

        # Rich Table UI
        table = Table(title="Router Decision")
        table.add_column("Destination Route", justify="center", style="cyan", no_wrap=True)
        table.add_column("Confidence Score", justify="center", style="magenta")
        table.add_row(ctx["route"].upper(), f"{confidence}%")
        console.print(table)
            
        return ctx

    async def _developer_node(self, ctx: dict) -> dict:
        prompt = ctx.get("masked_prompt", "").lower()
        
        # HITL Hook triggered by either mutation heuristics or the Security Interceptor
        if self._is_mutation_task(prompt) or ctx.get("security_hitl"):
            if not ctx.get("human_approved", False):
                console.print(Panel("[bold red]SECURITY HALT: Developer Task requires human approval.[/bold red]", border_style="red"))
                # Use to_thread to prevent blocking Uvicorn's event loop while waiting for CLI input
                approved = await asyncio.to_thread(Confirm.ask, "Do you approve this technical execution?")
                if approved:
                    ctx["human_approved"] = True
                    console.print("[bold green]Execution Approved by Developer.[/bold green]")
                else:
                    ctx["requires_human_approval"] = True
                    ctx["status"] = "Execution halted pending human approval."
                    return ctx

        # Interact with the Native Local RAG tool safely
        docs_context = await query_mcp_documentation(ctx.get("masked_prompt", ""))
        
        ctx["compiled_plan"] = f"Developer Structural Plan based on Local RAG Docs:\n{docs_context}"
        ctx["status"] = "Developer node execution completed."
        
        return ctx

    async def _task_execution_node(self, ctx: dict) -> dict:
        prompt = ctx.get("masked_prompt", "").lower()
        
        # HITL Hook triggered by either mutation heuristics or the Security Interceptor
        if self._is_mutation_task(prompt) or ctx.get("security_hitl"):
            if not ctx.get("human_approved", False):
                console.print(Panel("[bold red]SECURITY HALT: Lifestyle Task requires human approval.[/bold red]", border_style="red"))
                approved = await asyncio.to_thread(Confirm.ask, "Do you approve this action?")
                if approved:
                    ctx["human_approved"] = True
                    console.print("[bold green]Execution Approved by User.[/bold green]")
                else:
                    ctx["requires_human_approval"] = True
                    ctx["status"] = "Execution halted pending human approval."
                    return ctx

        ctx["final_response"] = f"Processed lifestyle task securely. Original prompt: {ctx.get('masked_prompt')}"
        ctx["status"] = "Task execution completed."
        
        return ctx

    async def arun(self, ctx: dict) -> dict:
        ctx = await self._router_node(ctx)
        
        if ctx.get("route") == "developer":
            ctx = await self._developer_node(ctx)
        elif ctx.get("route") == "task_execution":
            ctx = await self._task_execution_node(ctx)
            
        return ctx

routing_graph = RoutingGraph()
