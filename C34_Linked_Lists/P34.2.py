class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

# push_front(v):
# 1. Create a new node
# 2. If head is None, set head and tail to new node
# 3. Else, point new node's next to head, point head's prev to new node, update head to new node
# 4. Increment size

# pop_front():
# 1. If head is None, return None
# 2. Save head's value
# 3. Move head to head.next
# 4. If head is not None, set head.prev to None
# 5. Else, set tail to None
# 6. Decrement size
# 7. Return saved value

# push_back(v):
# 1. Create a new node
# 2. If head is None, set head and tail to new node
# 3. Else, point tail's next to new node, point new node's prev to tail, update tail to new node
# 4. Increment size

# pop_back():
# 1. If head is None, return None
# 2. Save tail's value
# 3. Move tail to tail.prev
# 4. If tail is not None, set tail.next to None
# 5. Else, set head to None
# 6. Decrement size
# 7. Return saved value

# n: number of nodes in the linked list
# T:
#   O(1): push_front, pop_front, push_back, pop_back, size - constant pointer updates or returning a stored value
#   O(n): contains - may traverse the entire list
# S:
#   O(1) for all methods
#   O(n) for the data structure overall

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0
    
    def size(self):
        return self._size
    
    def push_front(self, val):
        new = Node(val)
        if not self.head:
            self.head = self.tail = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new
        self._size += 1

    def pop_front(self):
        if not self.head:
            return None
        val = self.head.val
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self._size -= 1
        return val

    def push_back(self, val):
        new = Node(val)
        if not self.head:
            self.head = self.tail = new
        else:
            self.tail.next = new
            new.prev = self.tail
            self.tail = new
        self._size += 1

    def pop_back(self):
        if not self.head:
            return None
        val = self.tail.val
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        self._size -= 1
        return val

    def contains(self, val):
        curr = self.head
        while curr:
            if curr.val == val:
                return curr
            curr = curr.next
        return None



# # Doubly Linked List Design

# Implement a `DoublyLinkedList` class with the following methods:

# push_front(v):
#     Adds a node with value v at the beginning of the list.

# pop_front():
#     Removes the node at the beginning of the list and returns its value.
#     If the list is empty, returns None.

# push_back(v):
#     Adds a node with value v at the end of the list.

# pop_back():
#     Removes the node at the end of the list and returns its value.
#     If the list is empty, returns None.

# size():
#     Returns the number of nodes in the list.

# contains(v):
#     Return the first node with value v, if any, or null otherwise.

# Here are some examples:

# Example 1:
# list = DoublyLinkedList()
# list.push_front(1)  # List is now: 1
# list.push_front(2)  # List is now: 2<->1
# list.push_back(3)   # List is now: 2<->1<->3
# list.contains(2)    # Returns node with value 2
# list.contains(4)    # Returns None (value not found)
# list.size()         # Returns 3
# list.pop_front()    # Returns 2, list is now: 1<->3
# list.pop_back()     # Returns 3, list is now: 1

# Example 2:
# list = DoublyLinkedList()
# list.pop_front()    # Returns None (empty list)
# list.pop_back()     # Returns None (empty list)
# list.size()         # Returns 0

# This diagram shows the typical structure of a doubly linked list:

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/doubly-linked-list-design-1.png

# The `push_front()`, `pop_front()`, `push_back()`, `pop_back()`, and `size()` methods should all take `O(1)` time.

# Constraints:

# - You have to create the `Node` class with a `val` field and `prev` and `next` pointers. If your language is typed, you can either make the type of `val` be generic or integer.
# - The list can contain up to `10^5` nodes.