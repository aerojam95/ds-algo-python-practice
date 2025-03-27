# =============================================================================
# Modules
# =============================================================================

# Python
import unittest

# Testing
from selection_sort import selection_sort

# =============================================================================
# Tests
# =============================================================================

class TestSelectionSort(unittest.TestCase):
    """Unit tests for the Selection sort algorithm.

    Args:
        unittest (_type_): The unittest module.
    """

    def test_unsorted_list(self):
        self.assertEqual(selection_sort([5, 2, 8, 1, 3]), [1, 2, 3, 5, 8])

    def test_already_sorted_list(self):
        self.assertEqual(selection_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        self.assertEqual(selection_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_list_with_duplicates(self):
        self.assertEqual(selection_sort([4, 2, 4, 1, 3]), [1, 2, 3, 4, 4])

    def test_single_element_list(self):
        self.assertEqual(selection_sort([7]), [7])

    def test_empty_list(self):
        self.assertEqual(selection_sort([]), [])

    def test_all_same_elements(self):
        self.assertEqual(selection_sort([9, 9, 9, 9]), [9, 9, 9, 9])

if __name__ == "__main__":
    unittest.main()