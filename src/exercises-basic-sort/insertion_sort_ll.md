# Insertion Sort of LL

## Assignment

Write an `insertion_sort()` method in the `LinkedList` class that will sort the elements of a linked list in ascending order using the insertion sort algorithm.

The method should update the `head` and `tail` pointers of the linked list to reflect the new order of the nodes in the list.

You can assume that the input linked list will contain only integers. You should not use any additional data structures to sort the linked list.

## Input

The LinkedList object containing a linked list with unsorted elements (self).

## Output

`None`. The method sorts the linked list in place.

## Method Description

If the length of the linked list is less than `2`, the method returns and the list is assumed to be already sorted.

The first element of the linked list is treated as the sorted part of the list, and the second element is treated as the unsorted part of the list.

The first element of the sorted part of the list is then disconnected from the rest of the list, creating a new linked list with only one element.

The method then iterates through each remaining node in the unsorted part of the list.

For each node in the unsorted part of the list, the method determines its correct position in the sorted part of the list by comparing its value with the values of the other nodes in the sorted part of the list.

Once the correct position has been found, the node is inserted into the sorted part of the list at the appropriate position.

After all the nodes in the unsorted part of the list have been inserted into the sorted part of the list, the `head` and `tail` pointers of the linked list are updated to reflect the new order of the nodes in the list.

## Constraints

The linked list can contain duplicates.

The method should be implemented in the `LinkedList` class.

The method should not use any additional data structures to sort the linked list.
