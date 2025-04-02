# =============================================================================
# Functions
# =============================================================================

def max_subarray(nums: list[int]) -> int:
    """Finds the contiguous subarray with the largest sum.

    This function implements Kadane's algorithm to efficiently find the maximum 
    sum of any contiguous subarray in the given list.

    Args:
        nums (list[int]): A list of integers.

    Returns:
        int: The sum of the contiguous subarray with the largest sum.
    """
    if not nums:
        return 0
    
    max_sum = curr_sum = nums[0]
    
    for num in nums[1:]:
        curr_sum = max(nums, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
            
    return max_sum

