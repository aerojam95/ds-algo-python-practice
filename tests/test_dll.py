# =============================================================================
# Modules
# =============================================================================

# Python
from io import StringIO
import sys
import unittest


# Testing
from dll import Node, DoublyLinkedList

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
        self.assertIsNone(node.prev)

    def test_node_linking(self):
        """Test that a node can be linked to another node."""
        node1 = Node(1)
        node2 = Node(2)
        node1.next = node2
        node2.prev = node1
        self.assertEqual(node1.next, node2)
        self.assertEqual(node1.next.value, 2)
        self.assertEqual(node2.prev, node1)
        self.assertEqual(node2.prev.value, 1)

class TestDoublyLinkedList(unittest.TestCase):
    """Unit tests for the DoublyLinkedList class."""

    def test_append(self):
        """
        Test appending nodes to the doubly linked list.
        Ensures that nodes are appended correctly and length is updated.
        """
        dll = DoublyLinkedList(1)
        dll.append(2)
        dll.append(3)
        self.assertEqual(dll.head.value, 1)  # The first node should have value 1
        self.assertEqual(dll.tail.value, 3)  # The last node should have value 3
        self.assertEqual(dll.length, 3)  # The length should be 3 after appending two nodes

    def test_pop(self):
        """
        Test popping the last node from the doubly linked list.
        Ensures that the correct node is removed and tail is updated.
        """
        dll = DoublyLinkedList(1)
        dll.append(2)
        popped = dll.pop()
        self.assertEqual(popped.value, 2)  # The popped node should have value 2
        self.assertEqual(dll.tail.value, 1)  # The new tail should have value 1
        self.assertEqual(dll.length, 1)  # Length should be 1 after popping a node

    def test_prepend(self):
        """
        Test prepending a node to the doubly linked list.
        Ensures that nodes are added correctly at the head and length is updated.
        """
        dll = DoublyLinkedList(1)
        dll.prepend(0)
        self.assertEqual(dll.head.value, 0)  # The first node should have value 0
        self.assertEqual(dll.tail.value, 1)  # The last node should still have value 1
        self.assertEqual(dll.length, 2)  # Length should be 2 after prepending a node

    def test_pop_first(self):
        """
        Test popping the first node from the doubly linked list.
        Ensures that the correct node is removed and head is updated.
        """
        dll = DoublyLinkedList(1)
        dll.append(2)
        popped = dll.pop_first()
        self.assertEqual(popped.value, 1)  # The popped node should have value 1
        self.assertEqual(dll.head.value, 2)  # The new head should have value 2
        self.assertEqual(dll.length, 1)  # Length should be 1 after popping the first node

    def test_get(self):
        """
        Test retrieving a node at a specific index.
        Ensures that the node at the given index is returned correctly.
        """
        dll = DoublyLinkedList(1)
        dll.append(2)
        dll.append(3)
        node = dll.get(1)
        self.assertEqual(node.value, 2)  # The node at index 1 should have value 2

    def test_set_value(self):
        """
        Test setting the value of a node at a specific index.
        Ensures that the value is updated correctly.
        """
        dll = DoublyLinkedList(1)
        dll.append(2)
        dll.set_value(1, 5)
        self.assertEqual(dll.tail.value, 5)  # The value of the tail node should be updated to 5

    def test_insert(self):
        """
        Test inserting a new node at a specific index.
        Ensures that the node is inserted at the correct position and the list length is updated.
        """
        dll = DoublyLinkedList(1)
        dll.append(2)
        dll.append(3)
        dll.insert(1, 4)
        self.assertEqual(dll.get(1).value, 4)  # The node at index 1 should have value 4
        self.assertEqual(dll.length, 4)  # The length should be 4 after insertion

    def test_remove(self):
        """
        Test removing a node at a specific index.
        Ensures that the node is removed and the list is correctly updated.
        """
        dll = DoublyLinkedList(1)
        dll.append(2)
        dll.remove(0)
        self.assertEqual(dll.head.value, 2)  # The head should now have value 2
        self.assertEqual(dll.length, 1)  # The length should be 1 after removal
        
    def test_print_list(self):
        """Test printing the linked list values."""
        ll = DoublyLinkedList(1)
        ll.append(2)
        ll.append(3)

        # Capture printed output
        captured_output = StringIO()
        sys.stdout = captured_output
        ll.print_list()
        sys.stdout = sys.__stdout__  # Reset redirect

        output = captured_output.getvalue().strip().split("\n")
        self.assertEqual(output, ["1", "2", "3"])

if __name__ == '__main__':
    unittest.main()
