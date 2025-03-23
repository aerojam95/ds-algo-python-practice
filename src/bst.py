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
    
    def r_contains(self, value:int) -> bool:
        """Check if the binary search tree contains a given value using recursion.

        Args:
            value (int): The value to search for.

        Returns:
            bool: True if the value exists in the tree, otherwise False.
        """
        return self.__r_contains(self.root, value)
        
    def __r_contains(self, current: "Node", value: int) -> bool:
        """Recursive helper method to check if the binary search tree contains a given value.
        
        Args:
            current (Node): node to check if it contains the value.
            value (int): value to check if it exists in the tree.

        Returns:
            bool: True if the value exists in the tree, otherwise False.
        """
        if not current:
            return False
        if current.value == value:
            return True
        if value < current.value:
            return self.__r_contains(current.left, value)
        return self.__r_contains(current.right, value)
        
    def __r_insert(self, current_node: "Node", value: int) -> "Node":
        """Recursive helper method to insert a node into the binary search tree.

        Args:
            current_node (Node): current node to check if the value should be inserted.
            value (int): value of node to be added to binary search tree.

        Returns:
            Node: the current node after inserting the value.
        """
        if not current_node: 
            return Node(value)   
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value) 
        else:
            return current_node    
 
    def r_insert(self, value: int) -> None:
        """insert a node into the binary search tree using recursion.

        Args:
            value (int): value of node to be added to binary search tree.
        """
        if not self.root: 
            self.root = Node(value)
            return
        self.__r_insert(self.root, value) 
        
    def min_value(self, current: "Node") -> int:
        """Find the minimum value in the binary search tree.

        Args:
            current (Node): The current node to start the search from.

        Returns:
            int: The minimum value in the tree.
        """
        while current.left:
            current = current.left
        return current.value
    
    def delete_node(self, value: int) -> None:
        """Delete a node from the binary search tree.

        Args:
            value (int): The value of the node to delete.
        """
        if not self.root:
            return
        self.root = self._delete_node(self.root, value)
        
    def _delete_node(self, current: "Node", value: int) -> "Node":
        """Recursive helper method to delete a node from the binary search tree.

        Args:
            current (Node): The current node to check if it should be deleted.
            value (int): value of node to be deleted from the binary search tree.

        Returns:
            Node: The current node after deleting the value.
        """
        if not current:
            return None
        if value < current.value:
            current.left = self._delete_node(current.left, value)
        elif value > current.value:
            current.right = self._delete_node(current.right, value)
        else:
            if not current.left and not current.right:
                return None
            elif current.left is None:
                return current.right
            elif current.right is None:
                return current.left
            else:
                current.value = self.min_value(current.right)
                current.right = self._delete_node(current.right, current.value)
        return current
    
    def BFS(self) -> list[int]:
        """Breadth-first search traversal of the binary search tree.

        Returns:
            list[int]: The values of the nodes in the tree in BFS order.
        """
        if not self.root:
            return []
        
        current = self.root
        queue = []
        result = []
        queue.append(current)
        
        while queue:
            current = queue.pop(0)
            result.append(current.value)
            
            if current.left:
                queue.append(current.left)
                
            if current.right:
                queue.append(current.right)
                
        return result