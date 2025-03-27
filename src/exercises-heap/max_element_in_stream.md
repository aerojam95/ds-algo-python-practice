# Heap: Maximum Element in a Stream

Write a function named `stream_max` that takes as its input a list of integers (`nums`). The function should return a list of the same length, where each element in the output list is the maximum number seen so far in the input list.

More specifically, for each index `i` in the input list, the element at the same index in the output list should be the maximum value among the elements at indices `0` through `i` in the input list.

Use the provided `MaxHeap` class to solve this problem. You should not need to modify the `MaxHeap` class to complete this task.

Function Signature: `def stream_max(nums)`:

## Examples

If the input list is `[1, 3, 2, 5, 4]`, the function should return `[1, 3, 3, 5, 5]`.

*Explanation*:

At index `0`, the maximum number seen so far is `1`.

At index `1`, the maximum number seen so far is `3`.

At index `2`, the maximum number seen so far is still `3`.

At index `3`, the maximum number seen so far is `5`.

At index `4`, the maximum number seen so far is still `5`.

So, the output list is `[1, 3, 3, 5, 5]`.

Similarly, if the input list is `[7, 2, 4, 6, 1]`, the function should return `[7, 7, 7, 7, 7]`.

*Explanation*:

At each index, the maximum number seen so far is `7`.

So, the output list is `[7, 7, 7, 7, 7]`.

*Constraints*:

You may assume that the input list does not contain any `null` or undefined elements.
