# =============================================================================
# Functions
# =============================================================================

def item_in_common(list1:list[int], list2:list[int]) -> bool:
    """ Function takes two lists as input and returns True if there is at least one common item between the two lists, False otherwise.

    Args:
        list1 (list[int]): first list of integers
        list2 (list[int]): second list of integers
        
    Returns:
        bool: True if there is at least one common item between the two lists, False otherwise.
    """
    check_dict = {}
    for item in list1:
        check_dict[item] = True
        
    for item in list2:
        if check_dict.get(item):
            return True
    return False