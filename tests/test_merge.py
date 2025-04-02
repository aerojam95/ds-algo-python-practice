# =============================================================================
# Modules
# =============================================================================

# Python
import unittest

# Testing
from merge import merge

# =============================================================================
# Tests
# =============================================================================

class TestMerge(unittest.TestCase):
    """Unit tests for the merge function.

    Args:
        unittest (_type_): The unittest module.
    """
    def test_both_empty(self):
        self.assertEqual(merge([], []), [])
    
    def test_one_empty(self):
        self.assertEqual(merge([], [1, 2, 3]), [1, 2, 3])
        self.assertEqual(merge([1, 2, 3], []), [1, 2, 3])
    
    def test_no_overlap(self):
        self.assertEqual(merge([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])
    
    def test_with_duplicates(self):
        self.assertEqual(merge([1, 2, 2, 3], [2, 3, 4]), [1, 2, 2, 2, 3, 3, 4])
    
    def test_same_elements(self):
        self.assertEqual(merge([2, 2, 2], [2, 2]), [2, 2, 2, 2, 2])
    
    def test_already_merged(self):
        self.assertEqual(merge([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6])

if __name__ == "__main__":
    unittest.main()