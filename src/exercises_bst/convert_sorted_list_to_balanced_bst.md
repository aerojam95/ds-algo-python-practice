# BST: Convert Sorted List to Balanced BST

## Objective

The task is to develop a method that takes a sorted list of integers as input and constructs a height-balanced BST.

This involves creating a BST where the depth of the two subtrees of any node does not differ by more than one.

Achieving a height-balanced tree is crucial for optimizing the efficiency of tree operations, ensuring that the BST remains efficient for search, insertion, and deletion across all levels of the tree.

## Method Overview: `__sorted_list_to_bst`

*Input*: A sorted list of integers `nums`, provided in ascending order. The input list represents a sequential collection of elements to be transformed into a BST. The method also receives two additional parameters, `left` and `right`, which denotes the current segment of the list being processed.

*Process*: The method `__sorted_list_to_bst` employs a divide-and-conquer strategy to construct the BST. It identifies the middle element of the current list segment to serve as the subtree's root, ensuring that the resulting BST is height-balanced. The method recursively applies this logic to the left and right halves of the list, building up the BST from the bottom up.

*Output*: The root node of a height-balanced BST constructed from the sorted list. This node links to all other nodes in the BST, effectively representing the entire tree structure.

## Requirements

The BST must maintain the binary search tree property: for any given node, all values in the left subtree must be less than the node's value, and all values in the right subtree must be greater.

The resulting BST should be height-balanced to optimize the efficiency of subsequent operations performed on the tree.

## Implementation Details

The class `BinarySearchTree` encapsulates the functionality needed to construct and manage a BST, including the method `sorted_list_to_bst` which serves as the public interface for converting a sorted list into a BST.

The method `__sorted_list_to_bs` is a recursive helper function designed for internal use within the class. It directly supports the construction process by dividing the list and building the tree to ensure it is height-balanced.

If you are having difficulty understanding the process of repeatedly breaking the list in half recursively, it might be helpful to you to watch the Merge Sort section and then come back to this exercise.
