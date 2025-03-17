# =============================================================================
# Functions
# =============================================================================

def longest_consecutive_sequence(nums: list[int]) -> int:
    """Finds the length of the longest consecutive sequence in a list of integers.

    Args:
        list (list[int]): List of integers

    Returns:
        int: Length of the longest consecutive sequence
    """
    unique_nums = set(nums)
    longest_sequence = 0
    
    for num in unique_nums:
        if num - 1 not in unique_nums:
            current_num, current_sequence = num, 1
            
            while current_num + 1 in unique_nums:
                current_num += 1
                current_sequence += 1
                
            longest_sequence = max(longest_sequence, current_sequence)
            
    return longest_sequence