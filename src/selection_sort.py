# =============================================================================
# Functions
# =============================================================================

def selection_sort(my_list: list[int]) -> list[int]:
    """Sort a list using the selection sort algorithm.

    Args:
        my_list (list[int]): The list to sort. This list will be modified in-place.

    Returns:
        list[int]: The sorted list.
    """
    for i in range(0, len(my_list) - 1):
        min_index = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:
            my_list[i], my_list[min_index] = my_list[min_index], my_list[i]
                
    return my_list