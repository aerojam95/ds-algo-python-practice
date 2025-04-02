# =============================================================================
# Modules
# =============================================================================

# Python
import unittest

# Testing
from quick_sort import pivot, quick_sort, quick_sort_helper, swap

# =============================================================================
# Tests
# =============================================================================

class TestSwap(unittest.TestCase):
    """Unit test for the swap element of a list function.

    Args:
        unittest (_type_): The unittest module.
    """
    def test_swap(self):
        arr = [1, 2, 3, 4]
        swap(arr, 1, 3)
        self.assertEqual(arr, [1, 4, 3, 2])

class TestPivot(unittest.TestCase):
    """Unit test for the pivot function of quick sort algorithm.

    Args:
        unittest (_type_): The unittest module.
    """
    def test_pivot(self):
        arr = [4, 2, 7, 1, 3]
        pivot_index = pivot(arr, 0, len(arr) - 1)
        self.assertEqual(pivot_index, 3)

class TestQuickSortHelper(unittest.TestCase):
    """Unit test for the quick sort algorithm.

    Args:
        unittest (_type_): The unittest module.
    """
    def test_quick_sort_helper(self):
        arr = [4, 2, 7, 1, 3]
        sorted_arr = quick_sort_helper(arr, 0, len(arr) - 1)
        self.assertEqual(sorted_arr, [1, 2, 3, 4, 7])

class TestQuickSort(unittest.TestCase):
    """Unit test for the quick sort algorithm execution.

    Args:
        unittest (_type_): The unittest module.
    """
    def test_quick_sort(self):
        arr = [4, 2, 7, 1, 3]
        quick_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 7])

if __name__ == "__main__":
    unittest.main()
