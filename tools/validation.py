
VALID_BASES = {"A", "T", "G", "C"}
"""Set of valid DNA bases."""

def is_valid_dna(sequence: str) -> bool:
    """Checks if a DNA sequence is valid."""
    if not sequence:
        return False 
    return all(base in VALID_BASES for base in sequence)