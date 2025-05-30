# SLL: Partition List

Implement the `partition_list` member function for the LinkedList class, which partitions the list such that all nodes with values less than x come before nodes with values greater than or equal to `x`.

*Note*: This linked list class does NOT have a tail which will make this method easier to implement.

The original relative order of the nodes should be preserved.

## Details

The function `partition_lis`t takes an integer `x` as a parameter and modifies the current linked list in place according to the specified criteria. If the linked list is empty (i.e., `head` is `null`), the function should return immediately without making any changes.

### Example 1

*Input*:

Linked List: `3 -> 8 -> 5 -> 10 -> 2 -> 1` `x`: `5`

*Process*:

Values less than `5`: `3`, `2`, `1`

Values greater than or equal to `5`: `8`, `5`, `10`

*Output*:

Linked List: `3 -> 2 -> 1 -> 8 -> 5 -> 10`

### Example 2

*Input*:

Linked List: `1 -> 4 -> 3 -> 2 -> 5 -> 2` `x`: `3`

*Process*:

Values less than `3`: `1`, `2`, `2`

Values greater than or equal to `3`: `4`, `3`, `5`

*Output*:

Linked List: `1 -> 2 -> 2 -> 4 -> 3 -> 5`

## Tips

While traversing the linked list, maintain two separate chains: one for values less than `x` and one for values greater than or equal to `x`.

Use dummy nodes to simplify the handling of the heads of these chains.

After processing the entire list, connect the two chains to get the desired arrangement.

## Note 1

The solution must maintain the relative order of nodes. For instance, in the first example, even though `8` appears before `5` in the original list, the partitioned list must still have `8` before `5` as their relative order remains unchanged.

## Note 2

You must solve the problem WITHOUT MODIFYING THE VALUES in the list's nodes (i.e. only the nodes' next pointers may be changed)
