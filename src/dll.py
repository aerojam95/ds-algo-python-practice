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

    def pop(self) -> Node | None:
        """
        Remove and return the last node in the list.

        Returns:
            Node | None: The removed node, or None if the list is empty.
        """
        if self.length == 0:
            return None

        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value: int) -> bool:
        """
        Add a new node with the given value to the beginning of the list.

        Args:
            value (int): The value of the new node.

        Returns:
            bool: True if the operation was successful.
        """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self) -> Node | None:
        """
        Remove and return the first node in the list.

        Returns:
            Node | None: The removed node, or None if the list is empty.
        """
        if self.length == 0:
            return None

        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index: int) -> Node | None:
        """
        Retrieve a node at a given index.

        Args:
            index (int): The index of the node (0-based).

        Returns:
            Node | None: The node at the specified index, or None if out of bounds.
        """
        if index < 0 or index >= self.length:
            return None

        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index: int, value: int) -> bool:
        """
        Update the value of a node at a specific index.

        Args:
            index (int): The index of the node.
            value (int): The new value to set.

        Returns:
            bool: True if the update was successful, False if the index is out of bounds.
        """
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index: int, value: int) -> bool:
        """
        Insert a new node at a specific index.

        Args:
            index (int): The index to insert at (0-based).
            value (int): The value of the new node.

        Returns:
            bool: True if the insertion was successful, False otherwise.
        """
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

        self.length += 1
        return True

    def remove(self, index: int) -> Node | None:
        """
        Remove and return the node at a specific index.

        Args:
            index (int): The index of the node to remove.

        Returns:
            Node | None: The removed node, or None if out of bounds.
        """
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        temp = self.get(index)

        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None

        self.length -= 1
        return temp
