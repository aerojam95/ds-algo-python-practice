# =============================================================================
# Functions
# =============================================================================

def find_pairs(arr1: list[int], arr2: list[int], target: int) -> list[tuple[int, int]]:
    """Finds pairs from two arrays that sum up to a target value.

    Args:
        arr1 (list[int]): First array.
        arr2 (list[int]): Second array.
        target (int): Target value.

    Returns:
        list[tuple[int, int]]: Pairs of values from the two arrays that sum up to the target value.
    """
    arr1_set = set(arr1)     
    return [(target - num, num) for num in arr2 if (target - num) in arr1_set]