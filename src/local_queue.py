# =============================================================================
# Classes
# =============================================================================

class Node:
    """
    Represents a node in a queue.

    Attributes:
        value (int): The value stored in the node.
        next (Node | None): A reference to the next node in the list, or None if there is no next node.
    """

    def __init__(self, value) -> None:
        """
        Initialize a new node with a given value.

        Args:
            value (int): The value of the node.
        """
        self.value = value
        self.next: "Node | None" = None


class Queue:
    """
    Queue data structure using a singly linked list.

    This queue supports typical queue operations like enqueue and dequeue with
    O(1) time complexity for both operations.

    Attributes:
        first (Node | None): A reference to the first node in the queue.
        last (Node | None): A reference to the last node in the queue.
        length (int): The number of elements in the queue.
    """

    def __init__(self, value):
        """
        Initialize a queue with a single node containing the given value.

        Args:
            value (int): The initial value of the queue.
        """
        new_node = Node(value)
        self.first: "Node | None" = new_node
        self.last: "Node | None" = new_node
        self.length = 1

    def print_queue(self):
        """
        Print all values in the queue from front to back.

        Returns:
            None
        """
        if not self.first:
            print("Empty Stack")
            return
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value) -> bool:
        """
        Add a new value to the back of the queue.

        Args:
            value (int): The value to add to the queue.

        Returns:
            bool: True if the operation was successful.
        """
        new_node = Node(value)
        if not self.first:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True

    def dequeue(self) -> Node | None:
        """
        Remove and return the front value from the queue.

        Returns:
            Node | None: The removed node, or None if the queue is empty.
        """
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp
