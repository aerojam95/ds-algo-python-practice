# =============================================================================
# Modules
# =============================================================================

# Python 
from io import StringIO
import sys
import unittest

# Testing
from sll import Node, LinkedList

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


class TestLinkedList(unittest.TestCase):
    """Unit tests for the LinkedList class."""

    def test_linked_list_initialization(self):
        """Test that a linked list initializes correctly with a single node."""
        ll = LinkedList(5)
        self.assertEqual(ll.head.value, 5)
        self.assertEqual(ll.tail.value, 5)
        self.assertEqual(ll.length, 1)

    def test_append(self):
        """Test appending a node to the linked list."""
        ll = LinkedList(1)
        ll.append(2)
        self.assertEqual(ll.tail.value, 2)
        self.assertEqual(ll.length, 2)
        self.assertEqual(ll.head.next.value, 2)

    def test_pop(self):
        """Test popping the last node from the linked list."""
        ll = LinkedList(1)
        ll.append(2)
        popped_node = ll.pop()
        self.assertEqual(popped_node.value, 2)
        self.assertEqual(ll.tail.value, 1)
        self.assertEqual(ll.length, 1)
        self.assertIsNone(ll.head.next)

        ll.pop()  # Remove last node
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)
        self.assertEqual(ll.length, 0)

    def test_prepend(self):
        """Test prepending a node to the linked list."""
        ll = LinkedList(2)
        ll.prepend(1)
        self.assertEqual(ll.head.value, 1)
        self.assertEqual(ll.head.next.value, 2)
        self.assertEqual(ll.length, 2)

    def test_get(self):
        """Test getting a node by index."""
        ll = LinkedList(1)
        ll.append(2)
        ll.append(3)

        self.assertEqual(ll.get(0).value, 1)
        self.assertEqual(ll.get(1).value, 2)
        self.assertEqual(ll.get(2).value, 3)
        with self.assertRaises(IndexError):
            ll.get(5)  # Out of bounds

    def test_set_value(self):
        """Test setting the value of a node."""
        ll = LinkedList(1)
        ll.append(2)
        ll.append(3)

        result = ll.set_value(1, 99)
        self.assertTrue(result)
        self.assertEqual(ll.get(1).value, 99)

        with self.assertRaises(IndexError):
            ll.set_value(5, 100)  # Out of bounds

    def test_insert(self):
        """Test inserting a node at various positions."""
        ll = LinkedList(1)
        ll.append(3)
        ll.insert(1, 2)  # Insert at index 1
        self.assertEqual(ll.get(1).value, 2)
        self.assertEqual(ll.length, 3)

        ll.insert(0, 0)  # Insert at head
        self.assertEqual(ll.head.value, 0)
        self.assertEqual(ll.length, 4)

        ll.insert(4, 4)  # Insert at tail
        self.assertEqual(ll.tail.value, 4)
        self.assertEqual(ll.length, 5)

    def test_remove(self):
        """Test removing a node from different positions."""
        ll = LinkedList(1)
        ll.append(2)
        ll.append(3)

        removed_node = ll.remove(1)  # Remove middle node
        self.assertEqual(removed_node.value, 2)
        self.assertEqual(ll.length, 2)
        self.assertEqual(ll.head.next.value, 3)

        removed_node = ll.remove(0)  # Remove head
        self.assertEqual(removed_node.value, 1)
        self.assertEqual(ll.head.value, 3)

        removed_node = ll.remove(0)  # Remove last node
        self.assertEqual(removed_node.value, 3)
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)
        self.assertEqual(ll.length, 0)

    def test_reverse(self):
        """Test reversing the linked list."""
        ll = LinkedList(1)
        ll.append(2)
        ll.append(3)
        ll.append(4)
        ll.reverse()

        self.assertEqual(ll.head.value, 4)
        self.assertEqual(ll.head.next.value, 3)
        self.assertEqual(ll.head.next.next.value, 2)
        self.assertEqual(ll.tail.value, 1)

    def test_print_list(self):
        """Test printing the linked list values."""
        ll = LinkedList(1)
        ll.append(2)
        ll.append(3)

        # Capture printed output
        captured_output = StringIO()
        sys.stdout = captured_output
        ll.print_list()
        sys.stdout = sys.__stdout__  # Reset redirect

        output = captured_output.getvalue().strip().split("\n")
        self.assertEqual(output, ["1", "2", "3"])


if __name__ == "__main__":
    unittest.main()