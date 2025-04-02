# =============================================================================
# Functions
# =============================================================================

def find_max_min(my_list: list[int]) -> tuple[int, int]:
    """Finds the maximum and minimum values of an input list.

    Args:
        my_list (list[int]): list of integers.

    Returns:
        tuple[int, int]: Tuple of the maximum and minimum values of the list.
    """
    maxima = minima = my_list[0]
    
    for num in my_list[1:]:
        
        if num > maxima:
            maxima = num
            
        if num < minima:
            minima = num
            
    return (maxima, minima)