class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# n: number of nodes in the queue
# T: O(1) for all methods — push, pop, peek, size, empty
# S:
#   O(1) for all methods
#   O(n) for the data structure overall

class Queue: # FIFO: push at the tail, pop/peek at the head
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0
    
    def size(self):
        return self._size

    def pop(self):
        if not self.head:
            return None
        val = self.head.val
        self.head = self.head.next
        if not self.head:
            self.tail = None
        self._size -= 1
        return val

    def push(self, val):
        new = Node(val)
        if self.tail:
            self.tail.next = new
        self.tail = new
        if not self.head:
            self.head = new
        self._size += 1

    def peek(self):
        if self._size == 0:
            return None
        return self.head.val
    
    def empty(self):
        return self._size == 0
    


# # Linked-List-Based Queue

# Implement a `Queue` class using a singly linked list.

# It should support the following methods:

# push(v):
#     Adds a value v at the back of the queue.

# pop():
#     Removes the value at the front of the queue and returns its value.
#     If the queue is empty, returns None.

# peek():
#     Returns the value at the front of the queue without removing it.
#     If the queue is empty, returns None.

# size():
#     Returns the number of elements in the queue.

# empty():
#     Returns True if the queue is empty, False otherwise.

# Examples:

# Example 1:
# queue = Queue()
# queue.push(1)    # Queue is now: 1
# queue.push(2)    # Queue is now: 2->1
# queue.push(3)    # Queue is now: 3->2->1
# queue.peek()     # Returns 1
# queue.size()     # Returns 3
# queue.empty()    # Returns False
# queue.pop()      # Returns 1, queue is now: 3->2
# queue.pop()      # Returns 2, queue is now: 3
# queue.pop()      # Returns 3, queue is now empty
# queue.empty()    # Returns True

# Example 2:
# queue = Queue()
# queue.pop()      # Returns None (empty queue)
# queue.peek()     # Returns None (empty queue)
# queue.size()     # Returns 0
# queue.empty()    # Returns True

# Constraints:

# - If your language is typed, you can either make the type of the queue elements generic, or use integers.
# - All the methods should take `O(1)` time if the elements are integers.
# - The queue can contain up to `10^5` elements.