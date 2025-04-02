# =============================================================================
# Functions
# =============================================================================

def find_longest_string_1(my_list: list[str]) -> str:
    """Finds the longest string in a list of strings.

    Args:
        my_list (list[str]): list of strings.

    Returns:
        str: longest string from input.
    """
    longest = ""
    
    for word in my_list:
        
        if len(word) > len(longest):
            longest = word
            length = len(word)
            
    return longest

def find_longest_string_2(my_list: list[str]) -> str:
    """Finds the longest string in a list of strings.

    Args:
        my_list (list[str]): List of strings.

    Returns:
        str: Longest string from the input list.
    """
    return max(my_list, key=len) if my_list else ""