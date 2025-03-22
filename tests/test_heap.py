# =============================================================================
# Modules
# =============================================================================

# Python
import unittest

# Testing
from heap import MaxHeap, MinHeap

# =============================================================================
# Tests
# =============================================================================

class TestMaxHeap(unittest.TestCase):

    def test_insert_and_remove(self):
        heap = MaxHeap()
        for value in [10, 20, 5, 30]:
            heap.insert(value)
        self.assertEqual(heap.remove(), 30)
        self.assertEqual(heap.remove(), 20)
        self.assertEqual(heap.remove(), 10)
        self.assertEqual(heap.remove(), 5)
        self.assertIsNone(heap.remove())


class TestMinHeap(unittest.TestCase):

    def test_insert_and_remove(self):
        heap = MinHeap()
        for value in [10, 20, 5, 30]:
            heap.insert(value)
        self.assertEqual(heap.remove(), 5)
        self.assertEqual(heap.remove(), 10)
        self.assertEqual(heap.remove(), 20)
        self.assertEqual(heap.remove(), 30)
        self.assertIsNone(heap.remove())


if __name__ == "__main__":
    unittest.main()