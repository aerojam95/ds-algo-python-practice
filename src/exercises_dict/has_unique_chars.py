# =============================================================================
# Functions
# =============================================================================

def has_unique_chars(string: str) -> bool:
    """Checks if a string has all unique characters.

    Args:
        string (str): String to check.

    Returns:
        bool: True if the string has all unique characters, False otherwise.
    """
    unique_chars = set()
    for char in string:
        if char in unique_chars:
            return False
        unique_chars.add(char)
    return True