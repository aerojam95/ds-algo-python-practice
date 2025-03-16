# =============================================================================
# Classes
# =============================================================================

class Node:
    """Represents a node in a singly linked list."""

    def __init__(self, value: int) -> None:
        """
        Initialize a Node with a given value.

        Args:
            value (int): The value of the node.
        """
        self.value: int = value
        self.next: "Node | None" = None
        

class LinkedList:
    """Singly linked list implementation with basic operations."""
    def __init__(self, value: int) -> None:
        """
        Initialize a linked list with a single node.

        Args:
            value (int): The initial value of the linked list.
        """
        new_node = Node(value)
        self.head: Node | None = new_node
        self.tail: Node | None = new_node

    def append(self, value: int) -> bool:
        """
        Append a new node with the given value to the end of the linked list.

        Args:
            value (int): The value of the new node.

        Returns:
            bool: True if the operation was successful.
        """
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            assert self.tail is not None  # Ensuring tail is not None
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
        
    def find_middle_node(self) -> Node | None:
        """
        Returns the node in the middle of a SLL or the first of the two middle nodes of a list with an even number of nodes.

        Returns:
            Node | None: The middle node, or None if the list is empty.
        """
        if not self.head:
            return None
        if self.head == self.tail:
            return self.head
        pointer1, pointer2 = self.head, self.head
        while pointer2 and pointer2.next:
            pointer1 = pointer1.next
            pointer2 = pointer2.next.next
        return pointer1