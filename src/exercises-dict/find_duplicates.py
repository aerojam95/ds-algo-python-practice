# =============================================================================
# Functions
# =============================================================================

def find_duplicates(nums:list[int]) -> list[int]:
    """Using an array of integers nums, the function finds all the duplicates in the array using a hash table (dictionary).

    Args:
        nums (list[int]): list of numbers to check for duplicates.

    Returns:
        list[int]: list of numbers that are duplicates in the input list nums.
    """
    check_dict = {}
    duplicates = []
    
    for num in nums:
        check_dict[num] = check_dict.get(num, 0) + 1

    for key, count in check_dict.items():
        if count > 1:
            duplicates.append(key)
            
    return duplicates