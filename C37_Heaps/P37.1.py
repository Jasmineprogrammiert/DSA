# n: number of elements in the heap

# Operation       | Time     | Space
# push / pop      | O(log n) | O(log n)  (recursion depth)
# top / size      | O(1)     | O(1)
# heapify         | O(n)     | O(log n)

# S: O(n)
# S is the structure's standing footprint (all n elements); Space is the extra memory one call adds on top of it

class Heap:
    # If higher_priority(x, y) is True, x has higher priority than y
    def __init__(self, higher_priority=lambda x, y: x < y, heap=None):
        self.higher_priority = higher_priority
        self.heap = []
        if heap is not None:
            self.heap = heap.copy()
            self.heapify()

    def size(self):
        return len(self.heap)

    def top(self):
        if not self.heap:
            return None
        return self.heap[0]

    def push(self, elem):
        self.heap.append(elem)
        self.bubble_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None
        top = self.heap[0] # Promote the tail into the root, then sink it into place
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self.bubble_down(0)
        return top

    def heapify(self):
        # Half the nodes are parents and sit at the front, so the last parent is at index n//2 - 1
        # Sift each parent down, walking bottom-up: range(start, stop, step)
        for idx in range(len(self.heap) // 2 - 1, -1, -1):
            self.bubble_down(idx)

    def bubble_up(self, idx):
        if idx == 0:
            return # The root cannot be bubbled up
        parent_idx = self.parent(idx)
        if self.higher_priority(self.heap[idx], self.heap[parent_idx]):
            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            self.bubble_up(parent_idx)

    def bubble_down(self, idx):
        left_idx, right_idx = self.left_child(idx), self.right_child(idx)
        # Left fills before right, so no left child means no children at all
        is_leaf = left_idx >= len(self.heap)
        if is_leaf:
            return # Leaves cannot be bubbled down
        child_idx = left_idx # Index of the highest-priority child

        # Heap orders parent over child only, not siblings, so either child may rank higher
        if right_idx < len(self.heap) and self.higher_priority(self.heap[right_idx], self.heap[left_idx]):
            child_idx = right_idx

        if self.higher_priority(self.heap[child_idx], self.heap[idx]):
            self.heap[idx], self.heap[child_idx] = self.heap[child_idx], self.heap[idx]
            self.bubble_down(child_idx)

    def parent(self, idx):
        if idx == 0:
            return -1 # The root has no parent
        return (idx - 1) // 2

    def left_child(self, idx):
        return 2 * idx + 1

    def right_child(self, idx):
        return 2 * idx + 2

# # Implement A Heap

# Assume your language does not support a heap or priority queue. Implement a `Heap` class from scratch with:

# - A constructor that receives an optional list of elements to be heapified, and
# - Operations `size()`, `top()`, `push(elem)`, and `pop()`.

# Constraints:

# - The number of elements is at most `10^5`
# - If your language is typed, you can either make the type of the elements be generic, or use integers.
# - You can either make it a min-heap or make it generic by receiving a comparator function, `higher_priority`, in the constructor.

# This is the API:

# initialize(higher_priority, heap):
#   initializes a heap with the elements in `heap` (if any)
#   sets higher_priority() as the method to compare element priorities
#   higher_priority() should have this signature:
#   higher_priority(x, y):
#       returns true if x has higher priority than y, false otherwise

# push(elem): adds an element to the priority queue.

# pop(): removes and returns the highest-priority element.
# If the heap is empty, return null.

# top(): returns the highest-priority element without removing it.

# size(): returns the number of elements in the priority queue

# Example 1:
# heap = Heap(higher_priority: <)  # Min-heap
# heap.push(4)  # Elements ordered by priority: 4
# heap.push(8)  # Elements ordered by priority: 4, 8
# heap.push(2)  # Elements ordered by priority: 2, 4, 8
# heap.push(6)  # Elements ordered by priority: 2, 4, 6, 8
# heap.push(1)  # Elements ordered by priority: 1, 2, 4, 6, 8
# heap.pop()    # Returns 1. Elements ordered by priority: 2, 4, 6, 8
# heap.pop()    # Returns 2. Elements ordered by priority: 4, 6, 8
# heap.top()    # Returns 4. Elements ordered by priority: 4, 6, 8
# heap.pop()    # Returns 4. Elements ordered by priority: 6, 8
# heap.pop()    # Returns 6. Elements ordered by priority: 8
# heap.top()    # Returns 8. Elements ordered by priority: 8
# heap.pop()    # Returns 8.
# heap.size()   # Returns 0.
# heap.top()    # Returns null.
# heap.pop()    # Returns null.

# Example 2:
# heap = Heap(higher_priority: >, heap = [1, 8, 2, 6, 4])  # Max-heap
# heap.top()     # Returns 8. Elements ordered by priority: 8, 6, 4, 2, 1
# heap.pop()     # Returns 8. Elements ordered by priority: 6, 4, 2, 1
# heap.pop()     # Returns 6. Elements ordered by priority: 4, 2, 1
# heap.pop()     # Returns 4. Elements ordered by priority: 2, 1
