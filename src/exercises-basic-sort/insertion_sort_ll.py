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
    
    def insertion_sort(self) -> None:
        """
        Sort the linked list in-place using the insertion sort algorithm.

        The method iterates through the unsorted part of the list, 
        removing one node at a time and inserting it into the correct 
        position in the sorted part.
        """
        if self.length < 2:
            return
        
        sorted_head= self.head
        unsorted_head= self.head.next
        sorted_head.next = None
        
        while unsorted_head:
            current = unsorted_head
            unsorted_head= unsorted_head.next
            
            if current.value < sorted_head.value:
                current.next = sorted_head
                sorted_head= current
            else:
                search= sorted_head
                
                while search.next and current.value > search.next.value:
                    search= search.next
                    
                current.next = search.next
                search.next = current
                
                if current.next is None:
                    self.tail = current
                    
        self.head = sorted_head
                    
            
my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(7)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.insertion_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()