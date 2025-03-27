# =============================================================================
# Functions
# =============================================================================

def two_sum(nums: list[int], target: int) -> list[int]:
    """Function that returns the indices of the two numbers such that they add up to a specific target.
    
    Args:
        nums (list[int]): list of integers.
        target (int): target sum.
        
    Returns:
        list[int]: list of indices of the two numbers such that they add up to the target.
    """
    check_dict = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in check_dict:
            return [check_dict[complement], i]
        check_dict[num] = i
    return []
        