import logging
from rich.console import Console

logger = logging.getLogger(__name__)
console = Console()

class SecurityInterceptor:
    """
    Shadow-Mode Security Interceptor.
    Evaluates inbound prompts for risk using a simple heuristic keyword scoring system.
    If the risk score is high, it MUST flag the request for mandatory Human-in-the-Loop approval.
    """
    def __init__(self):
        self.high_risk_keywords = ["ignore", "override", "system", "prompt", "bypass", "delete", "remove", "unaligned", "hack"]
        self.risk_threshold = 30 # Out of 100

    def evaluate_risk(self, prompt: str) -> dict:
        """
        Returns a dict containing the risk_score and a boolean flag for HITL.
        """
        score = 0
        prompt_lower = prompt.lower()
        
        for keyword in self.high_risk_keywords:
            if keyword in prompt_lower:
                score += 15
                
        # Cap score at 100
        score = min(score, 100)
        requires_hitl = score >= self.risk_threshold
        
        return {
            "risk_score": score,
            "requires_hitl": requires_hitl,
            "reason": "High risk keywords detected." if requires_hitl else "Normal execution."
        }

security_interceptor = SecurityInterceptor()
