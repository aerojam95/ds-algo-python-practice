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
    
    def reverse(self) -> None:
        """
        Reverse the order of nodes in the doubly linked list.

        This operation modifies the list in place. After the reversal, the head
        and tail of the list will be swapped, and the order of the nodes will
        be reversed. If the list has fewer than two elements, no action is taken.

        Returns:
            None
        """
        if self.length <= 1:
            return
        current_node = self.head
        self.head, self.tail = self.tail, self.head
        while current_node:
            current_node.next, current_node.prev = current_node.prev, current_node.next
            current_node = current_node.prev
        return