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
    
    def is_valid_bst(self) -> bool:
        """Check if the binary search tree is a valid binary search tree.

        Returns:
            bool: True if the tree is a valid binary search tree, False otherwise.
        """
        elements = self.dfs_in_order()
        
        for i in range(1, len(elements)):
            if elements[i] <= elements[i - 1]:
                return False
            
        return True