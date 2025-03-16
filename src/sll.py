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

    def pop(self) -> Node | None:
        """
        Remove and return the last node in the linked list.

        Returns:
            Node | None: The removed node, or None if the list is empty.
        """
        if self.length == 0:
            return None

        temp = self.head
        pre = self.head

        while temp and temp.next:
            pre = temp
            temp = temp.next

        assert temp is not None  # Ensuring temp is not None
        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = self.tail = None

        return temp

    def prepend(self, value: int) -> bool:
        """
        Add a new node with the given value to the beginning of the linked list.

        Args:
            value (int): The value of the new node.

        Returns:
            bool: True if the operation was successful.
        """
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self) -> Node | None:
        """
        Remove and return the first node in the linked list.

        Returns:
            Node | None: The removed node, or None if the list is empty.
        """
        if self.length == 0 or not self.head:
            return None

        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        if self.length == 0:
            self.tail = None

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
            raise IndexError("Index out of range.")

        temp = self.head
        for _ in range(index):
            assert temp is not None  # Ensuring temp is not None
            temp = temp.next

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
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False

    def insert(self, index: int, value: int) -> bool:
        """
        Insert a new node at a specific index.

        Args:
            index (int): The index to insert at (0-based).
            value (int): The value of the new node.

        Returns:
            bool: True if insertion was successful, False otherwise.
        """
        if index < 0 or index > self.length:
            raise IndexError("Index out of range.")

        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        prev_node = self.get(index - 1)
        assert prev_node is not None  # Ensuring prev_node is not None
        new_node.next = prev_node.next
        prev_node.next = new_node
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
            raise IndexError("Index out of range.")

        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        prev_node = self.get(index - 1)
        assert prev_node is not None and prev_node.next is not None  # Ensuring nodes are not None
        temp = prev_node.next
        prev_node.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self) -> None:
        """
        Reverse the linked list in place.
        """
        if self.length < 2:
            return

        prev = None
        current = self.head
        self.head, self.tail = self.tail, self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
