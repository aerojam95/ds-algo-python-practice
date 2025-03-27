# =============================================================================
# Functions
# =============================================================================

def insertion_sort(my_list: list[int]) -> list[int]:
    """Sort a list using the insertion sort algorithm. O(n) when partially sorted my_list.

    Args:
        my_list (list[int]): The list to sort. This list will be modified in-place.

    Returns:
        list[int]: The sorted list.
    """
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1
        while j >= 0 and temp < my_list[j]:
            my_list[j + 1] =  my_list[j]
            my_list[j] = temp
            j -= 1
                
    return my_list