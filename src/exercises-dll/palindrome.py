# =============================================================================
# Classes
# =============================================================================

class Node:
    """Represents a node in a doubly linked list."""

    def __init__(self, value: int) -> None:
        """
        Initialize a node with a given value.

        Args:
            value (int): The value of the node.
        """
        self.value: int = value
        self.next: "Node | None" = None
        self.prev: "Node | None" = None


class DoublyLinkedList:
    """Doubly linked list implementation with basic operations."""

    def __init__(self, value: int) -> None:
        """
        Initialize a doubly linked list with a single node.

        Args:
            value (int): The initial value of the linked list.
        """
        new_node = Node(value)
        self.head: "Node | None" = new_node
        self.tail: "Node | None" = new_node
        self.length: int = 1

    def print_list(self) -> None:
        """Print all the values in the linked list."""
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value: int) -> bool:
        """
        Append a new node with the given value to the end of the list.

        Args:
            value (int): The value of the new node.

        Returns:
            bool: True if the operation was successful.
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def is_palindrome(self) -> bool:
        """
        Check if the doubly linked list is a palindrome.

        A list is considered a palindrome if the values of the nodes are the same
        when read from left to right as they are when read from right to left.

        Returns:
            bool: True if the list is a palindrome, False otherwise. 
                Returns True for empty or single-node lists as they are trivially palindromes.
        """
        if self.length <= 1:
            return True

        left = self.head
        right = self.tail

        # Compare values from the start and end of the list
        for _ in range(self.length // 2):
            if left.value != right.value:
                return False
            left = left.next
            right = right.prev

        return True