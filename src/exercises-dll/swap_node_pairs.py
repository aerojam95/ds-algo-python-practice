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
    
    def swap_pairs(self) -> None:
        """
        Swap every two adjacent nodes in the doubly linked list.

        This operation modifies the list in place by swapping the values of every 
        two adjacent nodes. If the list has an odd number of nodes, the last node 
        will remain in its original position.

        Returns:
            None
        """
        if self.length <= 1:
            return

        current = self.head
        prev_node = None

        # Traverse the list and swap adjacent nodes in pairs
        while current and current.next:
            node1 = current
            node2 = current.next

            # Adjust pointers to swap node1 and node2
            node1.next = node2.next
            node2.prev = node1.prev
            node2.next = node1
            node1.prev = node2

            # Update next node's prev pointer if it exists
            if node1.next:
                node1.next.prev = node1

            # Update the previous node to point to the new head of this swapped pair
            if prev_node:
                prev_node.next = node2
            else:
                self.head = node2  # Update head on first swap

            # Move to the next pair
            prev_node = node1
            current = node1.next
        return 
