# =============================================================================
# Modules
# =============================================================================

# Python
from io import StringIO
import sys
import unittest


# Testing
from stack import Node, Stack

# =============================================================================
# Tests
# =============================================================================

class TestNode(unittest.TestCase):
    """Unit tests for the Node class."""

    def test_node_initialization(self):
        """Test that a node initializes with the correct value and no next node."""
        node = Node(10)
        self.assertEqual(node.value, 10)
        self.assertIsNone(node.next)

    def test_node_linking(self):
        """Test that a node can be linked to another node."""
        node1 = Node(1)
        node2 = Node(2)
        node1.next = node2
        self.assertEqual(node1.next, node2)
        self.assertEqual(node1.next.value, 2)

class TestStack(unittest.TestCase):
    """Unit tests for the Stack class."""

    def test_push(self):
        """Test pushing a value onto the stack."""
        stack = Stack(10)
        self.assertEqual(stack.height, 1)
        stack.push(20)
        self.assertEqual(stack.height, 2)
        self.assertEqual(stack.top.value, 20)

    def test_pop(self):
        """Test popping a value from the stack."""
        stack = Stack(10)
        stack.push(20)
        popped_node = stack.pop()
        self.assertEqual(stack.height, 1)
        self.assertEqual(popped_node.value, 20)
        popped_node = stack.pop()
        self.assertEqual(stack.height, 0)
        self.assertIsNone(stack.pop())

    def test_print_stack(self):
        """Test printing the stack."""
        stack = Stack(1)
        stack.push(2)
        stack.push(3)
        # Capture printed output
        captured_output = StringIO()
        sys.stdout = captured_output
        stack.print_stack()
        sys.stdout = sys.__stdout__  # Reset redirect

        output = captured_output.getvalue().strip().split("\n")
        self.assertEqual(output, ["3", "2", "1"])

    def test_empty_pop(self):
        """Test popping from an empty stack."""
        stack = Stack(10)
        stack.pop()
        self.assertIsNone(stack.pop())

    def test_height_after_operations(self):
        """Test the height of the stack after several operations."""
        stack = Stack(10)
        stack.push(20)
        stack.push(30)
        self.assertEqual(stack.height, 3)
        stack.pop()
        self.assertEqual(stack.height, 2)
        stack.push(40)
        self.assertEqual(stack.height, 3)

if __name__ == '__main__':
    unittest.main()