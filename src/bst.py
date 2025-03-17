# =============================================================================
# Classes
# =============================================================================

class Node:
    """Represents a node in a binary search tree."""

    def __init__(self, value: int) -> None:
        """
        Initialize a node with a given value.

        Args:
            value (int): The value of the node.
        """
        self.value: int = value
        self.left: "Node | None" = None
        self.right: "Node | None" = None
        
class BinarySearchTree():
    """Binary search tree implementation with basic operations.
    """
    def __init__(self) -> None:
        """
        Initialize a binary search tree.
        """
        self.root = None
        
    def insert(self, value: int) -> bool:
        """insert a node into the binary search tree.

        Args:
            value (int): value of node to be added to binary search tree.

        Returns:
            bool: True if the insertion was successful, False if the value already exists.
        """
        new_node = Node(value)
        
        if not self.root:
            self.root = new_node
            return True
        
        current = self.root
        while True:
            if value == current.value:
                return False
            
            if value < current.value:
                if not current.left:
                    current.left = new_node
                    return True
                current = current.left
            else:
                if not current.right:
                    current.right = new_node
                    return True
                current = current.right
        
        
    def contains(self, value: int) -> bool:
        """Check if the binary search tree contains a given value.

        Args:
            value (int): The value to search for.

        Returns:
            bool: True if the value exists in the tree, otherwise False.
        """
        current = self.root
        while current:
            if value == current.value:
                return True
            if value < current.value:
                current = current.left
            else:
                current = current.right
        return False
    