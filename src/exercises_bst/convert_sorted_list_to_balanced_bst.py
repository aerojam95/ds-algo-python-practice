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
        
    # The 'is_balanced' and 'inorder_traversal' methods will 
    # be used to test your code
    def is_balanced(self, node = None):
        def check_balance(node: Node):
            if node is None:
                return True, -1
            left_balanced, left_height = check_balance(node.left)
            if not left_balanced:
                return False, 0
            right_balanced, right_height = check_balance(node.right)
            if not right_balanced:
                return False, 0
            balanced = abs(left_height - right_height) <= 1
            height = 1 + max(left_height, right_height)
            return balanced, height

        balanced, _ = check_balance(self.root if node is None else node)
        return balanced
        
    def inorder_traversal(self, node: Node = None):
        if node is None:
            node = self.root
        result = []
        self._inorder_helper(node, result)
        return result
    
    def _inorder_helper(self, node: Node, result):
        if node:
            self._inorder_helper(node.left, result)
            result.append(node.value)
            self._inorder_helper(node.right, result)
                
                
    def sorted_list_to_bst(self, nums: list[int]) -> None:
        self.root = self.__sorted_list_to_bst(nums, 0, len(nums) - 1)

    def __sorted_list_to_bst(self, nums: list[int], left: int, right: int) -> Node | None:
        """Generate a balanced binary search tree from a sorted list of integers.

        Args:
            nums (list[int]): A sorted list of integers.
            left (int): left index of the list.
            right (int): right index of the list.

        Returns:
            Node | None: The root node of the balanced binary search tree.
        """
        if left > right:
            return None
        middle = (left + right) // 2
        current = Node(nums[middle])
        current.left = self.__sorted_list_to_bst(nums, left, middle - 1)
        current.right = self.__sorted_list_to_bst(nums, middle + 1, right)
        return current