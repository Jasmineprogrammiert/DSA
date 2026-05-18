# Problem 34.4 - Linked-List-Based Queue
# Implement a Queue class using a singly linked list.
#
# push(v): Adds a value v at the back of the queue.
# pop(): Removes and returns the value at the front. Returns None if empty.
# peek(): Returns the value at the front without removing it. Returns None if empty.
# size(): Returns the number of elements in the queue.
# empty(): Returns True if the queue is empty, False otherwise.
#
# Example 1:
# queue = Queue()
# queue.push(1)   # 1
# queue.push(2)   # 2->1
# queue.push(3)   # 3->2->1
# queue.peek()    # Returns 1
# queue.size()    # Returns 3
# queue.empty()   # Returns False
# queue.pop()     # Returns 1, queue: 3->2
# queue.pop()     # Returns 2, queue: 3
# queue.pop()     # Returns 3, queue empty
# queue.empty()   # Returns True
#
# Example 2:
# queue = Queue()
# queue.pop()     # Returns None
# queue.peek()    # Returns None
# queue.size()    # Returns 0
# queue.empty()   # Returns True
#
# Constraints:
# - All methods should be O(1)
# - Up to 10^5 elements