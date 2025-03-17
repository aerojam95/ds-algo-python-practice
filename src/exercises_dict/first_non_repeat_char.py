# =============================================================================
# Functions
# =============================================================================

def first_non_repeating_char(string:str) -> str | None:
    """Function finds the first non-repeating character in the given string using a hash table (dictionary).

    Args:
        string (str): input string to search over.

    Returns:
        str | None: char that is the first non-repeating char, otherwise None if no non-repeating char exists.
    """
    check_dict = {}
    
    for char in string:
        check_dict[char] = check_dict.get(char, 0) + 1
    
    for char in string:
        if check_dict[char] == 1:
            return char
    return None