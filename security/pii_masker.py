import re
import hashlib
from typing import Tuple, Dict

class PIIMasker:
    """
    A utility class to mask Personally Identifiable Information (PII) from strings.
    Replaces identified PII with a structural placeholder and provides a lookup vault
    to reverse the masking if necessary.
    """

    def __init__(self):
        # Define regex patterns for different PII types.
        # Order matters mildly if patterns overlap, but these are fairly distinct.
        self.patterns = {
            # Standard email format
            'EMAIL': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
            
            # SSN: ddd-dd-dddd
            'SSN': r'\b\d{3}-\d{2}-\d{4}\b',
            
            # Policy IDs: 5 digits followed by a hyphen and 3 or more uppercase letters
            'POLICY_ID': r'\b\d{5}-[A-Z]{3,}\b',
            
            # Phone: International and local formats
            # Matches formats like +1-800-555-1234, (800) 555-1234, 800-555-1234, etc.
            'PHONE': r'(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b'
        }
        
        # Compile patterns for better performance
        self.compiled_patterns = {
            name: re.compile(pattern) for name, pattern in self.patterns.items()
        }

    def sanitize_input(self, raw_prompt: str) -> Tuple[str, Dict[str, str]]:
        """
        Sanitizes the input string by replacing PII with secure placeholders.
        
        Args:
            raw_prompt (str): The inbound text containing potential PII.
            
        Returns:
            Tuple[str, Dict[str, str]]: A tuple containing the sanitized string and
            a dictionary mapping the generated placeholders back to the original PII.
        """
        if not isinstance(raw_prompt, str):
            raise TypeError(f"Expected string for raw_prompt, got {type(raw_prompt).__name__}")
            
        sanitized_prompt = raw_prompt
        lookup_vault: Dict[str, str] = {}

        # Process each type of PII
        for pii_type, pattern in self.compiled_patterns.items():
            # Find all unique matches in the text.
            # Using set ensures we only process identical strings once,
            # though str.replace() replaces all instances globally anyway.
            matches = set(pattern.findall(sanitized_prompt))
            
            for match in matches:
                if not match:
                    continue
                    
                # Create a deterministic short hash to use in the placeholder
                # This ensures the identical PII gets the exact same token placeholder
                match_hash = hashlib.sha256(match.encode('utf-8')).hexdigest()[:8]
                placeholder = f"[[MASKED_{pii_type}_{match_hash}]]"
                
                # Replace all occurrences of this specific match in the text
                sanitized_prompt = sanitized_prompt.replace(match, placeholder)
                
                # Store the mapping in our look-up vault for reverse lookup
                lookup_vault[placeholder] = match
                
        return sanitized_prompt, lookup_vault
