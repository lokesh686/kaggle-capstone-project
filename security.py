import re

def scrub_pii(text: str) -> str:
    """
    Security Feature (Rubric Requirement)
    Scrubs Credit Card numbers and Social Security Numbers from text before sending to LLM.
    """
    # Scrub 16-digit credit cards
    text = re.sub(r'\b(?:\d[ -]*?){13,16}\b', '[REDACTED CREDIT CARD]', text)
    # Scrub SSN
    text = re.sub(r'\b\d{3}-\d{2}-\d{4}\b', '[REDACTED SSN]', text)
    return text
