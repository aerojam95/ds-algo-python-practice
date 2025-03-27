# =============================================================================
# Modules
# =============================================================================

# Python
import unittest

# Testing
from bubble_sort import bubble_sort

# =============================================================================
# Tests
# =============================================================================

class TestBubbleSort(unittest.TestCase):
    """Unit tests for the Bubble sort algorithm."""

    def test_unsorted_list(self):
        self.assertEqual(bubble_sort([4, 2, 5, 1, 3]), [1, 2, 3, 4, 5])

    def test_already_sorted_list(self):
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_list_with_duplicates(self):
        self.assertEqual(bubble_sort([3, 1, 2, 3, 1]), [1, 1, 2, 3, 3])

    def test_single_element_list(self):
        self.assertEqual(bubble_sort([42]), [42])

    def test_empty_list(self):
        self.assertEqual(bubble_sort([]), [])

    def test_all_same_elements(self):
        self.assertEqual(bubble_sort([7, 7, 7, 7]), [7, 7, 7, 7])

if __name__ == "__main__":
    unittest.main()