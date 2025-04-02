# =============================================================================
# Functions
# =============================================================================

def remove_duplicates(my_list: list[int]) -> int:
    """Removes duplicates in a sorted list in-place and returns the count of unique elements.

    Args:
        my_list (list[int]): A sorted list of integers.

    Returns:
        int: The number of unique elements.
    """
    if not my_list:
        return 0
    
    index = 0
    
    for i in range(1, len(my_list)):
        
        if my_list[i] != my_list[index]:
            index += 1
            my_list[index] = my_list[i]
            
    return index + 1
            