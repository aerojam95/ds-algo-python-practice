# =============================================================================
# Modules
# =============================================================================

# Python
import unittest

# Testing
from insertion_sort import insertion_sort

# =============================================================================
# Tests
# =============================================================================

class TestInsertionSort(unittest.TestCase):
    """Unit tests for the Insertion sort algorithm.
    
    Args:
        unittest (_type_): The unittest module.
    """

    def test_unsorted_list(self):
        self.assertEqual(insertion_sort([4, 2, 7, 1, 3]), [1, 2, 3, 4, 7])

    def test_already_sorted(self):
        self.assertEqual(insertion_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        self.assertEqual(insertion_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_with_duplicates(self):
        self.assertEqual(insertion_sort([3, 1, 2, 3, 1]), [1, 1, 2, 3, 3])

    def test_single_element(self):
        self.assertEqual(insertion_sort([99]), [99])

    def test_empty_list(self):
        self.assertEqual(insertion_sort([]), [])

    def test_all_same(self):
        self.assertEqual(insertion_sort([5, 5, 5, 5]), [5, 5, 5, 5])

if __name__ == "__main__":
    unittest.main()