# =============================================================================
# Functions
# =============================================================================

def rotate(nums: list[int], k: int) -> None:
    """Rotates the list to the right by k steps in-place.

    This function modifies `nums` by shifting elements to the right `k` times.
    If `k` is greater than the list length, it is reduced modulo `len(nums)`.

    Args:
        nums (list[int]): The list of integers to rotate.
        k (int): Number of steps to rotate the list to the right.

    Returns:
        None: The function modifies `nums` in place.
    """
    if not nums or k == 0:
        return

    k %= len(nums)
    if k == 0:
        return 

    nums[:] = nums[-k:] + nums[:-k]

        