# =============================================================================
# Functions
# =============================================================================

def subarray_sum(nums: list[int], target: int) -> list[int]:
    """Finds the indices of a contiguous subarray in nums that add up to the target sum using a hash table (dictionary).

    Args:
        nums (list[int]): a list of integers representing the input array.
        target (int): an integer representing the target sum.

    Returns:
        list[int]: a list of two integers representing the starting and ending indices of the subarray that adds up to the target sum.
    """
    check_sum = {0:-1}
    current_sum = 0
    
    for i, num in enumerate(nums):
        current_sum += num
        target_sum = current_sum - target
        if target_sum in check_sum:
            return [check_sum[target_sum] + 1, i]
        check_sum[current_sum] = i
                
    return []