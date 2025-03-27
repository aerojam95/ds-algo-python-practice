# =============================================================================
# Functions
# =============================================================================

def remove_duplicates(my_list: list[int]) -> list[int]:
    """Removes all the duplicates from the list.

    Args:
        my_list (list[int]): List of integers.

    Returns:
        list[int]: List of integers with duplicates removed.
    """
    unique_numbers = set()
    return [number for number in my_list if not (number in unique_numbers or unique_numbers.add(number))]