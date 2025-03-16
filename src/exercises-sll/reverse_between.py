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
        
    def reverse_between(self, start_index: int, end_index: int) -> None:
        """
        Reverse a portion of the linked list between two indices (1-based).

        Args:
            start_index (int): The starting index of the sublist to reverse.
            end_index (int): The ending index of the sublist to reverse.

        Returns:
            None: The linked list is modified in place.
        """
        if self.length <= 1 or start_index >= end_index:
            return

        dummy = Node(0)
        dummy.next = self.head
        previous = dummy

        # Move `previous` to one node before the start index
        for _ in range(start_index):
            if not previous.next:
                return  # Start index out of bounds
            previous = previous.next

        current = previous.next

        # Reverse nodes within the given range
        for _ in range(end_index - start_index):
            if not current or not current.next:
                return  # End index out of bounds

            node_to_move = current.next
            current.next = node_to_move.next
            node_to_move.next = previous.next
            previous.next = node_to_move

        self.head = dummy.next
