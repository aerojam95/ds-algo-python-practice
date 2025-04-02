# =============================================================================
# Modules
# =============================================================================

# Python
import unittest

# Testing
from merge_sort import merge_sort

# =============================================================================
# Tests
# =============================================================================

class TestMergeSort(unittest.TestCase):
    """Unit tests for the merge sort algorithm.

    Args:
        unittest (_type_): The unittest module.
    """
    def test_empty_list(self):
        self.assertEqual(merge_sort([]), [])
    
    def test_single_element(self):
        self.assertEqual(merge_sort([5]), [5])
    
    def test_sorted_list(self):
        self.assertEqual(merge_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
    
    def test_reverse_sorted_list(self):
        self.assertEqual(merge_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
    
    def test_unsorted_list(self):
        self.assertEqual(merge_sort([3, 1, 4, 1, 5, 9, 2]), [1, 1, 2, 3, 4, 5, 9])
    
    def test_list_with_duplicates(self):
        self.assertEqual(merge_sort([4, 2, 4, 2, 1]), [1, 2, 2, 4, 4])
    
    def test_large_numbers(self):
        self.assertEqual(merge_sort([1000, 500, 100, 50, 10]), [10, 50, 100, 500, 1000])
    
    def test_negative_numbers(self):
        self.assertEqual(merge_sort([-3, -1, -4, -2, -5]), [-5, -4, -3, -2, -1])
    
    def test_mixed_numbers(self):
        self.assertEqual(merge_sort([3, -1, 4, -2, 5, 0]), [-2, -1, 0, 3, 4, 5])
    
if __name__ == "__main__":
    unittest.main()
