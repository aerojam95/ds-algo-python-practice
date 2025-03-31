# =============================================================================
# Functions
# =============================================================================

def swap(my_list: list[int], index1: int, index2: int) -> None:
    """Swaps two elements in a list.

    Args:
        my_list (list[int]): The list in which to swap elements.
        index1 (int): first index of the element to swap.
        index2 (int): second index of the element to swap.
    """
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp

def pivot(my_list: list[int], pivot_index: int, end_index: int) -> int:
    """
    Selects a pivot element from the list. The pivot is chosen as the last element.

    Args:
        my_list (list[int]): The list from which to select the pivot.
        pivot_index (int): Index of pivot element.
        end_index (int): Last element of my_list.

    Returns:
        int: The pivot element.
    """
    swap_index = pivot_index
    
    for i in range(pivot_index + 1, end_index + 1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)

    swap(my_list, pivot_index, swap_index)
    
    return swap_index

def quick_sort_helper(my_list: list[int], left: int, right: int) -> list[int]:
    """Performs the quick sort algorithm on a list recursively.

    Args:
        my_list (list[int]): list to sort.
        left (int): lower index of the list.
        right (int): upper index of the list.

    Returns:
        list[int]: sorted list.
    """
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index - 1)
        quick_sort_helper(my_list, pivot_index + 1, right)
    
    return my_list

def quick_sort(my_list: list[int]) -> list[int]:
    """Quick sort algorithm.

    Args:
        my_list (list[int]): list to sort. Sorted in place.

    Returns:
        list[int]: sorted list.
    """
    quick_sort_helper(my_list, 0, len(my_list)-1)