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
    
    def selection_sort(self) -> None:
        """
        Sort the linked list in-place using the selection sort algorithm.

        The sorting is performed by finding the minimum value node in the unsorted
        part of the list and swapping it with the current node.
        """
        if self.length < 2:
            return
        
        current = self.head
        
        while current:
            min_node = current
            next_node = current.next
            
            while next_node:
                
                if next_node.value < min_node.value:
                    min_node = next_node
                next_node = next_node.next
            
            if current.value != min_node.value:
                current.value, min_node.value = min_node.value, current.value

            current = current.next