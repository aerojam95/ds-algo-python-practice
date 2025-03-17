# =============================================================================
# Modules
# =============================================================================

# Python
import unittest

# Testing
from hash_tables import HashTable

# =============================================================================
# Tests
# =============================================================================

class TestHashTable(unittest.TestCase):

    def setUp(self):
        """Set up a new HashTable instance before each test."""
        self.ht = HashTable()

    def test_set_and_get_item(self):
        """Test inserting and retrieving key-value pairs."""
        self.ht.set_item("apple", 100)
        self.ht.set_item("banana", 200)
        
        self.assertEqual(self.ht.get_item("apple"), 100)
        self.assertEqual(self.ht.get_item("banana"), 200)

    def test_get_non_existing_key(self):
        """Test retrieving a non-existent key should return None."""
        self.assertIsNone(self.ht.get_item("grape"))

    def test_handle_collisions(self):
        """Test handling of hash collisions by inserting multiple values at the same index."""
        # Assuming small table size increases likelihood of collision
        small_ht = HashTable(size=3)
        small_ht.set_item("a", 1)
        small_ht.set_item("b", 2)
        small_ht.set_item("c", 3)  # Likely to collide
        
        self.assertEqual(small_ht.get_item("a"), 1)
        self.assertEqual(small_ht.get_item("b"), 2)
        self.assertEqual(small_ht.get_item("c"), 3)

    def test_keys(self):
        """Test retrieving all stored keys."""
        self.ht.set_item("dog", 50)
        self.ht.set_item("cat", 75)
        self.ht.set_item("bird", 30)
        
        keys = self.ht.keys()
        self.assertCountEqual(keys, ["dog", "cat", "bird"])  # Order-independent check

if __name__ == "__main__":
    unittest.main()