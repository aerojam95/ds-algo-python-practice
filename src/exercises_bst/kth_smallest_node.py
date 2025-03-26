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
                
    def dfs_in_order(self) -> list[int]:
        """Depth-first search in-order traversal of the binary search tree. Goes left, root, right. Down the left side of the tree first. 

        Returns:
            list[int]: The values of the nodes in the tree in DFS in-order.
        """
        results = []
        
        def traverse(current: "Node") -> None:
            if current.left:
                traverse(current.left)
            results.append(current.value)
            if current.right:
                traverse(current.right)
                
        if self.root:
            traverse(self.root)
            
        return results
                
    def kth_smallest(self, element: int) -> int:
        """Get the kth smallest element in the binary search tree.

        Args:
            element (int): The kth smallest element to find.

        Returns:
            int: The kth smallest element.
        """
        elements = self.dfs_in_order()
        
        if len(elements) <= 0:
            return None
        
        if element < 1 or element > len(elements):
            return None
        
        return elements[element - 1]