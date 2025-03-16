# SLL: Remove Duplicates

You are given a singly linked list that contains integer values, where some of these values may be duplicated.

*Note*:* this linked list class does NOT have a `tail` which will make this method easier to implement.

Your task is to implement a method called `remove_duplicates()` within the LinkedList class that removes all duplicate values from the list.

Your method should not create a new list, but rather modify the existing list in-place, preserving the relative order of the nodes.

You can implement the `remove_duplicates()` method in two different ways:

Using a `Set` - This approach will have a time complexity of O(n), where n is the number of nodes in the linked list. You are allowed to use the provided Set data structure in your implementation.

Without using a `Set` - This approach will have a time complexity of O(n^2), where n is the number of nodes in the linked list. You are not allowed to use any additional data structures for this implementation.

Here is the method signature you need to implement:

`def remove_duplicates(self):`

## Example

*Input*:

LinkedList: `1 -> 2 -> 3 -> 1 -> 4 -> 2 -> 5`

*Output*:

LinkedList: `1 -> 2 -> 3 -> 4 -> 5`
