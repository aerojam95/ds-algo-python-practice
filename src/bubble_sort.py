# =============================================================================
# Functions
# =============================================================================

def bubble_sort(my_list: list[int]) -> list[int]:
    """Sort a list using the bubble sort algorithm.

    Args:
        my_list (list[int]): The list to sort. This list will be modified in-place.

    Returns:
        list[int]: The sorted list.
    """
    for i in range(len(my_list), 0, -1):
        for j in range(1, i):
            if my_list[j - 1] > my_list[j]:
                my_list[j - 1], my_list[j] = my_list[j], my_list[j - 1]
                
    return my_list