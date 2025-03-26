# BST: Validate BST

You are tasked with writing a method called `is_valid_bst` in the `BinarySearchTree` class that checks whether a binary search tree is a valid binary search tree.

Your method should use the `dfs_in_order` method to get the node values of the binary search tree in ascending order, and then check whether each node value is greater than the previous node value.

If the node values are not sorted in ascending order, the method should return `False`, indicating that the binary search tree is not valid.

If all node values are sorted in ascending order, the method should return `True`, indicating that the binary search tree is a valid binary search tree.
