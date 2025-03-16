# =============================================================================
# Classes
# =============================================================================

class Node:
    """
    Represents a node in a stack.

    Attributes:
        value (int): The value stored in the node.
        next (Node | None): A reference to the next node in the stack, or None if there is no next node.
    """

    def __init__(self, value) -> None:
        """
        Initialize a new node with a given value.

        Args:
            value (int): The value of the node.
        """
        self.value = value
        self.next: "Node | None" = None


class Stack:
    """
    Stack data structure using a singly linked list.

    This stack supports typical stack operations like push and pop with
    O(1) time complexity for both operations.

    Attributes:
        top (Node | None): A reference to the top node of the stack.
        height (int): The number of elements in the stack.
    """

    def __init__(self, value) -> None:
        """
        Initialize a stack with a single node containing the given value.

        Args:
            value (int): The initial value of the stack.
        """
        new_node = Node(value)
        self.top: Node | None = new_node
        self.height = 1

    def print_stack(self) -> None:
        """
        Print all values in the stack from top to bottom.

        Returns:
            None
        """
        if not self.top:
            print("Empty Stack")
            return
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def push(self, value) -> bool:
        """
        Add a new value to the top of the stack.

        Args:
            value (int): The value to add to the stack.

        Returns:
            bool: True if the operation was successful.
        """
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.height += 1
        return True

    def pop(self) -> Node | None:
        """
        Remove and return the top value from the stack.

        Returns:
            Node | None: The removed node, or None if the stack is empty.
        """
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp
