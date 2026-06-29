import json
import logging
import os
import time
from pathlib import Path

logger = logging.getLogger(__name__)

LOGS_DIR = Path(__file__).parent.parent / "logs"
AUDIT_FILE = LOGS_DIR / "audit_log.json"

def initialize_audit_log():
    """Ensure the logs directory and JSON array exist."""
    os.makedirs(LOGS_DIR, exist_ok=True)
    if not AUDIT_FILE.exists():
        with open(AUDIT_FILE, "w", encoding="utf-8") as f:
            json.dump([], f)

def log_audit_record(record: dict):
    """
    Appends a structured JSON record to logs/audit_log.json.
    Must include: Timestamp, Original Prompt, Masked Prompt, Risk Score, Route Taken, and Response Time.
    """
    initialize_audit_log()
    try:
        with open(AUDIT_FILE, "r+", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
            
            # Auto-inject UTC timestamp if not provided
            if "Timestamp" not in record:
                record["Timestamp"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
                
            data.append(record)
            
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
            
    except Exception as e:
        logger.error(f"Failed to write audit log: {e}")
