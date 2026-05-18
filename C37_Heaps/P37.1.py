# Problem 37.1 - Implement a Heap
# Implement a Heap class from scratch with:
# - Constructor: optional list of elements to heapify, optional comparator
# - push(elem): adds an element
# - pop(): removes and returns highest-priority element (None if empty)
# - top(): returns highest-priority element without removing (None if empty)
# - size(): returns number of elements
#
# Example 1 (min-heap):
# heap = Heap(higher_priority: <)
# heap.push(4), heap.push(8), heap.push(2), heap.push(6), heap.push(1)
# heap.pop() -> 1, heap.pop() -> 2
# heap.top() -> 4 (after popping 4)
# heap.pop() -> 6, heap.top() -> 8, heap.pop() -> 8
# heap.size() -> 0, heap.top() -> None, heap.pop() -> None
#
# Example 2 (max-heap with heapify):
# heap = Heap(higher_priority: >, heap = [1,8,2,6,4])
# heap.top() -> 8
# heap.pop() -> 8, heap.pop() -> 6, heap.pop() -> 4
#
# Constraints:
# - Up to 10^5 elements