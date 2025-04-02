# =============================================================================
# Functions
# =============================================================================

def remove_element(nums: list[int], val: int) -> int:
    """Remove occurrences of val from nums in place and return the new length.

    Args:
        nums (list[int]): List of integers.
        val (int): Integer to remove.

    Returns:
        int: Length of the modified list.
    """
    write_index = 0

    for num in nums:
        if num != val:
            nums[write_index] = num
            write_index += 1

    nums[:] = nums[:write_index]
    
    return write_index