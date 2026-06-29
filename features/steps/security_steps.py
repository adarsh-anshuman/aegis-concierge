import sys
from pathlib import Path
from behave import given, when, then

# Ensure the root project directory is in the path for imports
sys.path.append(str(Path(__file__).parent.parent.parent))

from security.threat_scan import ThreatScanner
from security.pii_masker import PIIMasker

@given('the ThreatScanner is initialized')
def step_impl(context):
    context.scanner = ThreatScanner()

@when('a malicious prompt "{prompt}" is evaluated')
def step_impl(context, prompt):
    context.is_threat = context.scanner.is_injection(prompt)

@when('a clean prompt "{prompt}" is evaluated')
def step_impl(context, prompt):
    context.is_threat = context.scanner.is_injection(prompt)

@then('the scanner should flag it as an injection')
def step_impl(context):
    assert context.is_threat is True, "Scanner failed to flag threat."

@then('the scanner should not flag it')
def step_impl(context):
    assert context.is_threat is False, "Scanner falsely flagged a clean prompt."

@given('the PIIMasker is initialized')
def step_impl(context):
    context.masker = PIIMasker()

@when('a prompt containing an email "{email}" is sanitized')
def step_impl(context, email):
    context.sanitized, context.vault = context.masker.sanitize_input(f"Contact me at {email} please.")

@then('the output should contain a masked email placeholder')
def step_impl(context):
    assert "[[MASKED_EMAIL_" in context.sanitized, f"Output did not contain masked email: {context.sanitized}"
    assert len(context.vault) == 1, "Vault should contain exactly 1 mapped element."
