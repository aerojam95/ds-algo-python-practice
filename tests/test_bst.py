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
        
    def test_r_insert_root(self):
        """Test recursive insertion of the root node."""
        self.bst.r_insert(10)
        self.assertEqual(self.bst.root.value, 10)

    def test_r_insert_left_and_right(self):
        """Test recursive insertion to left and right of the root."""
        self.bst.r_insert(10)
        self.bst.r_insert(5)
        self.bst.r_insert(15)

        self.assertEqual(self.bst.root.left.value, 5)
        self.assertEqual(self.bst.root.right.value, 15)

    def test_r_contains_existing_values(self):
        """Test r_contains returns True for existing values."""
        for val in [10, 5, 15]:
            self.bst.r_insert(val)
        
        self.assertTrue(self.bst.r_contains(10))
        self.assertTrue(self.bst.r_contains(5))
        self.assertTrue(self.bst.r_contains(15))

    def test_r_contains_non_existing_values(self):
        """Test r_contains returns False for values not in the tree."""
        self.bst.r_insert(10)
        self.assertFalse(self.bst.r_contains(100))
        self.assertFalse(self.bst.r_contains(0))
        self.assertFalse(self.bst.r_contains(-10))
        
    def test_delete_node(self):
        """Test deleting nodes with 0, 1, and 2 children."""
        # Build tree:
        #        10
        #       /  \
        #      5    15
        #     / \     \
        #    3   7     20
        for val in [10, 5, 15, 3, 7, 20]:
            self.bst.insert(val)

        # Delete leaf node (no children)
        self.bst.delete_node(3)
        self.assertIsNone(self.bst.root.left.left)

        # Delete node with one child
        self.bst.delete_node(15)
        self.assertEqual(self.bst.root.right.value, 20)

        # Delete node with two children
        self.bst.delete_node(5)
        self.assertEqual(self.bst.root.left.value, 7)
        self.assertIsNone(self.bst.root.left.left)  # 3 was deleted earlier
        
    def test_bfs_traversal(self):
        """Test breadth-first search traversal returns correct order."""
        # Tree structure:
        #        10
        #       /  \\
        #      5    15
        #     / \\     \\
        #    3   7     20
        for val in [10, 5, 15, 3, 7, 20]:
            self.bst.insert(val)

        expected_bfs = [10, 5, 15, 3, 7, 20]
        self.assertEqual(self.bst.BFS(), expected_bfs)
        
    def test_pre_order(self):
        """Test breadth-first search traversal returns correct order."""
        # Tree structure:
        #        10
        #       /  \\
        #      5    15
        #     / \\     \\
        #    3   7     20
        for val in [10, 5, 15, 2, 7, 20]:
            self.bst.insert(val)
        expected_pre_order = [10, 5, 2, 7, 15, 20]
        self.assertEqual(self.bst.dfs_pre_order(), expected_pre_order)

    def test_in_order(self):
        """Test breadth-first search traversal returns correct order."""
        # Tree structure:
        #        10
        #       /  \\
        #      5    15
        #     / \\     \\
        #    3   7     20
        for val in [10, 5, 15, 2, 7, 20]:
            self.bst.insert(val)
        expected_in_order = [2, 5, 7, 10, 15, 20]
        self.assertEqual(self.bst.dfs_in_order(), expected_in_order)

    def test_post_order(self):
        """Test breadth-first search traversal returns correct order."""
        # Tree structure:
        #        10
        #       /  \\
        #      5    15
        #     / \\     \\
        #    3   7     20
        for val in [10, 5, 15, 2, 7, 20]:
            self.bst.insert(val)
        expected_post_order = [2, 7, 5, 20, 15, 10]
        self.assertEqual(self.bst.dfs_post_order(), expected_post_order)

if __name__ == '__main__':
    unittest.main()