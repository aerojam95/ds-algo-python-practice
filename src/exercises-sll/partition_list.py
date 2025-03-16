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
        self.length: int = 1

    def print_list(self) -> None:
        """
        Print all the values in the linked list.
        """
        if not self.head:
            print("Empty List")
            return

        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

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
    
    def make_empty(self) -> None:
        """
        Reset the linked list to an empty state.
        
        Sets the head and tail to None and resets the length to zero.
        """
        self.head = None
        self.tail = None
        self.length = 0
        
    def partition_list(self, x) -> None:
        """
        Rearrange the linked list so that all nodes with values less than `x`
        appear before nodes greater than or equal to `x`, while maintaining relative order.

        Args:
            x (int): The partition value.

        Returns:
            None: The linked list is modified in place.
        """
        if not self.head:
            return None
        dummy1 = LinkedList(0)
        dummy2 = LinkedList(0)
        prev1, prev2 = dummy1, dummy2
        temp_node = self.head
        while temp_node:
            if temp_node.value < x:
                prev1.next = temp_node
                prev1 = temp_node
            else:
                prev2.next = temp_node
                prev2 = temp_node
            temp_node = temp_node.next
        prev1.next = None
        prev2.next = None
        prev1.next = dummy2.next
        self.head = dummy1.next
        return dummy1