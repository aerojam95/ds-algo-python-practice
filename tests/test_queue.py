# =============================================================================
# Modules
# =============================================================================

# Python
from io import StringIO
import sys
import unittest


# Testing
from local_queue import Node, Queue

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
        
class TestQueue(unittest.TestCase):
    """Unit tests for the Queue class."""

    def test_enqueue(self):
        """Test enqueueing a value onto the queue."""
        queue = Queue(10)
        self.assertEqual(queue.length, 1)
        queue.enqueue(20)
        self.assertEqual(queue.length, 2)
        self.assertEqual(queue.last.value, 20)

    def test_dequeue(self):
        """Test dequeueing a value from the queue."""
        queue = Queue(10)
        queue.enqueue(20)
        dequeued_node = queue.dequeue()
        self.assertEqual(queue.length, 1)
        self.assertEqual(dequeued_node.value, 10)
        dequeued_node = queue.dequeue()
        self.assertEqual(queue.length, 0)
        self.assertIsNone(queue.dequeue())

    def test_print_queue(self):
        """Test printing the queue."""
        queue = Queue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        # Capture printed output
        captured_output = StringIO()
        sys.stdout = captured_output
        queue.print_queue()
        sys.stdout = sys.__stdout__  # Reset redirect

        output = captured_output.getvalue().strip().split("\n")
        self.assertEqual(output, ["1", "2", "3"])

    def test_empty_dequeue(self):
        """Test dequeueing from an empty queue."""
        queue = Queue(10)
        queue.dequeue()
        self.assertIsNone(queue.dequeue())

    def test_length_after_operations(self):
        """Test the length of the queue after several operations."""
        queue = Queue(10)
        queue.enqueue(20)
        queue.enqueue(30)
        self.assertEqual(queue.length, 3)
        queue.dequeue()
        self.assertEqual(queue.length, 2)
        queue.enqueue(40)
        self.assertEqual(queue.length, 3)

if __name__ == '__main__':
    unittest.main()