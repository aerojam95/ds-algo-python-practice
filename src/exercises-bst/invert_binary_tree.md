# BST: Invert Binary Tree

## Objective

Write a method to invert (or mirror) a binary tree. This means that for every node in the binary tree, you will swap its left and right children.

## Method Signature: `def __invert_tree(self, node)`

## Input

`node`: A `Node` object representing the root of a binary tree. The `Node` class has attributes `value`, `left`, and `right`, where value is the value stored in the `node`, and `left` and `right` are pointers to the `node`'s `left` and `right` children, respectively.

## Output

The `root` node of the inverted binary tree.

## Requirements

The method must be recursive. It should work by traversing the tree and swapping the left and right children of every node encountered.

If the input tree is empty (i.e., `node` is `None`), the method should return `None`.

The inversion should happen in-place, meaning you should not create a new tree but instead modify the existing tree structure.

The method should handle binary trees of any size and structure, ensuring that every node's left and right children are swapped.
