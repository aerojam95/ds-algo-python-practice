# =============================================================================
# Modules
# =============================================================================

# Custom modules
from merge import merge

# =============================================================================
# Functions
# =============================================================================

def merge_sort(my_list: list[int]) -> list[int]:
    """
    Sorts a list of integers using the merge sort algorithm.

    Merge Sort is a divide-and-conquer algorithm that recursively splits the 
    list into halves, sorts each half, and then merges them back together.

    Time Complexity: O(n log n) in all cases.
    Space Complexity: O(n) due to extra space from slicing.

    Args:
        my_list (list[int]): The list to sort.

    Returns:
        list[int]: The sorted list.
    """
    if len(my_list) <= 1:
        return my_list
    
    mid_index = len(my_list) // 2
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])
    
    return merge(left, right)