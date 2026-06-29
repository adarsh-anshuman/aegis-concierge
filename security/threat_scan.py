import re

class ThreatScanner:
    """
    Inspects inbound strings for prompt injection patterns and system override attempts.
    Implements structural checks for high-frequency injection tokens and execution vectors.
    """

    def __init__(self):
        # High-frequency injection tokens (case-insensitive checks)
        self.injection_patterns = [
            r"ignore\s+(all\s+)?previous\s+instructions",
            r"system\s+override",
            r"you\s+are\s+now\s+unaligned",
            r"disregard\s+(all\s+)?rules",
            r"bypass\s+security"
        ]

        # Execution vectors (e.g., malicious Python imports or shell escapes)
        self.execution_vectors = [
            r"os\.system\s*\(",
            r"subprocess\.",
            r"rm\s+-rf",
            r"import\s+os\b",
            r"import\s+sys\b",
            r"import\s+subprocess\b",
            r"eval\s*\(",
            r"exec\s*\("
        ]

        # Compile regex patterns for efficient scanning
        self.compiled_injections = [
            re.compile(pattern, re.IGNORECASE) for pattern in self.injection_patterns
        ]
        
        # Execution vectors are generally case-sensitive (like python commands), 
        # but making them case-insensitive adds a layer of safety against obfuscated prompts.
        # We will keep shell/python commands case-sensitive for exact structural match 
        # but it can be adjusted based on strictness requirements.
        self.compiled_executions = [
            re.compile(pattern) for pattern in self.execution_vectors
        ]

    def is_injection(self, user_input: str) -> bool:
        """
        Returns True if a prompt injection signature or execution vector matches the input.
        """
        if not isinstance(user_input, str):
            return False

        # Scan for semantic injection tokens
        for pattern in self.compiled_injections:
            if pattern.search(user_input):
                return True

        # Scan for technical execution vectors
        for pattern in self.compiled_executions:
            if pattern.search(user_input):
                return True

        return False

    def get_fallback_message(self) -> str:
        """
        Returns the standard compliance string when an injection is detected.
        """
        return "Security policy violation: Request blocked by local Aegis Threat Scan."
