# =============================================================================
# Classes
# =============================================================================

class MaxHeap:
    """
    A MaxHeap implementation using a list to store elements.

    The MaxHeap maintains the max-heap property: the value of each parent node
    is greater than or equal to the values of its children. The largest element
    is always at the root.

    This class supports insertion of elements and removal of the maximum element.

    Attributes:
        heap (list[int]): List representation of the heap.
    """

    def __init__(self):
        """
        Initialize an empty MaxHeap.
        """
        self.heap = []

    def _left_child(self, index: int) -> int:
        """
        Get the index of the left child.

        Args:
            index (int): Index of the parent node.

        Returns:
            int: Index of the left child.
        """
        return 2 * index + 1

    def _right_child(self, index: int) -> int:
        """
        Get the index of the right child.

        Args:
            index (int): Index of the parent node.

        Returns:
            int: Index of the right child.
        """
        return 2 * index + 2

    def _parent(self, index: int) -> int:
        """
        Get the index of the parent node.

        Args:
            index (int): Index of the child node.

        Returns:
            int: Index of the parent node.
        """
        return (index - 1) // 2

    def _swap(self, i: int, j: int) -> None:
        """
        Swap two elements in the heap.

        Args:
            i (int): Index of the first element.
            j (int): Index of the second element.
        """
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _sink_down(self, index: int) -> None:
        """
        Sink the element at the given index down the heap until the max-heap
        property is restored.

        Args:
            index (int): Index of the element to sink.
        """
        while True:
            largest = index
            left = self._left_child(index)
            right = self._right_child(index)

            if left < len(self.heap) and self.heap[left] > self.heap[largest]:
                largest = left
            if right < len(self.heap) and self.heap[right] > self.heap[largest]:
                largest = right

            if largest == index:
                break

            self._swap(index, largest)
            index = largest

    def insert(self, value: int) -> None:
        """
        Insert a new value into the heap.

        Args:
            value (int): Value to insert.
        """
        self.heap.append(value)
        index = len(self.heap) - 1
        while index > 0 and self.heap[index] > self.heap[self._parent(index)]:
            self._swap(index, self._parent(index))
            index = self._parent(index)

    def remove(self) -> int | None:
        """
        Remove and return the maximum value (the root) from the heap.

        Returns:
            int | None: The removed value, or None if the heap is empty.
        """
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return root
    
# =============================================================================
# Functions
# =============================================================================

def find_kth_smallest(nums: list[int], k: int) -> int | None:
    """Find the kth smallest number in the nums list.

    Args:
        nums (list[int]): A list of integers.
        k (int): The k-th position (1-based index) of the smallest element to find.

    Returns:
        int | None: value of kth smallest element or None if k is out of bounds.
    """
    if not nums or k < 1 or k > len(nums):
        return None
    
    heap = MaxHeap()
    
    for num in nums:
        heap.insert(num)
        
        if len(heap.heap) > k:
            heap.remove()

    return heap.remove()
    
    
nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 7

print(find_kth_smallest(nums, k))