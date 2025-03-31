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
    
    def merge(self, sll2: "LinkedList") -> "LinkedList":
        """
        Merge two sorted linked lists into a new sorted linked list.

        Args:
            sll2 (LinkedList): The second sorted linked list to merge.

        Returns:
            LinkedList: A new sorted linked list containing all elements from both input lists.
        """
        if not self.head and not sll2.head:
            return self
        
        dummy = Node(0)
        current = dummy
        pointer1 = self.head
        pointer2 = sll2.head
        
        while pointer1 and pointer2:
            
            if pointer1.value < pointer2.value:
                current.next = pointer1
                pointer1 = pointer1.next
            else:
                current.next = pointer2
                pointer2 = pointer2.next
            current = current.next
            
        if pointer1:
            current.next = pointer1
            
        if pointer2:
            current.next = pointer2

            
        self.head = dummy.next
        temp = self.head
        
        while temp.next:
            temp = temp.next
            
        self.tail = temp
        self.length += sll2.length
        
        return self