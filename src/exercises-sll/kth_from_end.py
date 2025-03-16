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
    
# =============================================================================
# Functions
# =============================================================================

def find_kth_from_end(ll, k: int) -> Node | None:
    """
    Find the k-th node from the end of a singly linked list.

    Uses the two-pointer technique: one pointer advances `k` steps first, 
    then both move together until the lead pointer reaches the end.

    Args:
        ll (LinkedList): The linked list to search in.
        k (int): The position from the end (1-based index).

    Returns:
        Node | None: The k-th node from the end, or None if k is out of bounds.
    """
    slow, fast = ll.head, ll.head
    for _ in range(0, k):
        if not fast:
            return None
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    return slow