import time
from fastapi import FastAPI
from pydantic import BaseModel
from rich.console import Console
from rich.panel import Panel

from security.threat_scan import ThreatScanner
from security.pii_masker import PIIMasker
from security.security_interceptor import security_interceptor
from skills.family_manager.routing_graph import routing_graph
from utils.audit_logger import log_audit_record

# Concept 2: Security Features - PII Masking, Threat Scanning, and Audit Logging.

app = FastAPI(title="Aegis Concierge API")
console = Console()

threat_scanner = ThreatScanner()
pii_masker = PIIMasker()

class ChatRequest(BaseModel):
    user_prompt: str

@app.post("/api/v1/chat")
async def chat_endpoint(request: ChatRequest):
    start_time = time.time()
    raw_prompt = request.user_prompt
    
    console.print("\n" + "="*50)
    console.print(f"[bold blue]New Request Initiated[/bold blue]")

    # 1. Threat Scan
    if threat_scanner.is_injection(raw_prompt):
        console.print(Panel(f"Threat Detected: {raw_prompt}", title="Threat Scanner - BLOCKED", border_style="red"))
        return {"status": "error", "response": threat_scanner.get_fallback_message()}

    # 2. PII Masking
    masked_prompt, vault = pii_masker.sanitize_input(raw_prompt)
    if masked_prompt != raw_prompt:
        console.print(Panel(f"Original: {raw_prompt}\nMasked: {masked_prompt}", title="PII Masker - DATA SANITIZED", border_style="yellow"))
    else:
        console.print(Panel(masked_prompt, title="Clean Prompt - NO PII DETECTED", border_style="green"))

    # 3. Security Interceptor (Shadow-Mode Risk Scoring)
    risk_data = security_interceptor.evaluate_risk(masked_prompt)
    risk_color = "red" if risk_data["requires_hitl"] else "cyan"
    console.print(f"[bold {risk_color}]Risk Score: {risk_data['risk_score']}/100[/bold {risk_color}] - {risk_data['reason']}")

    # 4. Cognitive Routing
    ctx = {
        "masked_prompt": masked_prompt,
        "security_hitl": risk_data["requires_hitl"],
        "human_approved": False
    }

    final_ctx = await routing_graph.arun(ctx)

    # Rehydrate if a final response was generated
    final_response_text = final_ctx.get("compiled_plan") or final_ctx.get("final_response") or final_ctx.get("status")

    # Re-hydrate the masked tokens using the local vault
    for original_text, hash_key in vault.items():
        if final_response_text and hash_key in final_response_text:
            final_response_text = final_response_text.replace(hash_key, original_text)

    # 5. Enterprise Audit Logging
    response_time_ms = round((time.time() - start_time) * 1000, 2)
    audit_record = {
        "Original Prompt": raw_prompt,
        "Masked Prompt": masked_prompt,
        "Risk Score": risk_data["risk_score"],
        "Route Taken": final_ctx.get("route", "unknown"),
        "Response Time ms": response_time_ms
    }
    log_audit_record(audit_record)
    
    console.print(f"[bold green]Request Complete. Response Time: {response_time_ms}ms[/bold green]")
    console.print("="*50 + "\n")

    return {
        "status": "success" if not final_ctx.get("requires_human_approval") else "halted",
        "response": final_response_text,
        "route_taken": final_ctx.get("route", "unknown"),
        "requires_human_approval": final_ctx.get("requires_human_approval", False)
    }
