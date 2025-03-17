# =============================================================================
# Modules
# =============================================================================

# Python
import unittest

# Testing
from bst import Node, BinarySearchTree

# =============================================================================
# Tests
# =============================================================================

class TestNode(unittest.TestCase):
    """Unit tests for the Node class."""

    def test_node_initialization(self):
        """Test that a node initializes with the correct value and no left/right nodes."""
        node = Node(10)
        self.assertEqual(node.value, 10)
        self.assertIsNone(node.left)
        self.assertIsNone(node.right)

    def test_node_linking(self):
        """Test that a node can be linked to another node."""
        node1 = Node(1)
        node2 = Node(2)
        node1.left = node2
        self.assertEqual(node1.left, node2)
        self.assertEqual(node1.left.value, 2)
        
class TestBinarySearchTree(unittest.TestCase):
    
    def setUp(self):
        """Set up a new BST for each test."""
        self.bst = BinarySearchTree()

    def test_insert_root(self):
        """Test inserting a value as the root node."""
        self.assertTrue(self.bst.insert(10))
        self.assertEqual(self.bst.root.value, 10)

    def test_insert_left_and_right(self):
        """Test inserting values to the left and right of the root."""
        self.bst.insert(10)
        self.assertTrue(self.bst.insert(5))  # Left child
        self.assertTrue(self.bst.insert(15)) # Right child
        
        self.assertEqual(self.bst.root.left.value, 5)
        self.assertEqual(self.bst.root.right.value, 15)

    def test_contains_existing_value(self):
        """Test that contains() returns True for inserted values."""
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)

        self.assertTrue(self.bst.contains(10))
        self.assertTrue(self.bst.contains(5))
        self.assertTrue(self.bst.contains(15))

    def test_contains_non_existing_value(self):
        """Test that contains() returns False for values not in the tree."""
        self.bst.insert(10)
        self.assertFalse(self.bst.contains(20))
        self.assertFalse(self.bst.contains(0))
        self.assertFalse(self.bst.contains(-5))

    def test_contains_empty_tree(self):
        """Test contains() on an empty tree."""
        self.assertFalse(self.bst.contains(10))

if __name__ == '__main__':
    unittest.main()