# =============================================================================
# Functions
# =============================================================================

def merge(list1: list[int], list2: list[int]) -> list[int]:
    """Merge two sorted lists into a single sorted list.

    Args:
        list1 (list[int]): The first sorted list.
        list2 (list[int]): The second sorted list.

    Returns:
        list[int]: A new sorted list containing all elements from both input lists.
    """
    combined = []
    i = j = 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
            
    combined.extend(list1[i:])
    combined.extend(list2[j:])
            
    return combined