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
        
    def __r_insert(self, current_node, value):
        if current_node == None: 
            return Node(value)   
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        elif value > current_node.value:  # Changed to elif to avoid comparing twice if equal
            current_node.right = self.__r_insert(current_node.right, value) 
        return current_node    

    def r_insert(self, value):
        if self.root == None: 
            self.root = Node(value)
        else:
            self.__r_insert(self.root, value)  

    def invert(self):
        self.root = self.__invert_tree(self.root)
        
    def __invert_tree(self, node: Node) -> Node:
        """Invert a binary tree.

        Args:
            node (Node): The node of the tree around which to invert.

        Returns:
            Node: The root node of the inverted tree.
        """
        if not node:
            return None
        node.left, node.right = self.__invert_tree(node.right), self.__invert_tree(node.left)
        return node