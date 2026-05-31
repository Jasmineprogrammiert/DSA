class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# push_front(v):
# 1. Create a new node
# 2. Point new node's next to head
# 3. Update head to new node
# 4. Increment size

# pop_front():
# 1. If head is None, return None
# 2. Save head's value
# 3. Move head to head.next
# 4. Decrement size
# 5. Return saved value

# push_back(v):
# 1. Create a new node
# 2. If head is None, set head to new node
# 3. Else, traverse to the last node and point last node's next to new node
# 4. Increment size

# pop_back():
# 1. If head is None, return None
# 2. If head.next is None, save head's value, set head to None, decrement size, return it
# 3. Traverse to the second-to-last node
# 4. Save last node's value
# 5. Set second-to-last node's next to None
# 6. Decrement size
# 7. Return saved value

# n: number of nodes in the linked list
# T:
#   O(1): push_front, pop_front, size - constant pointer updates or returning a stored value
#   O(n): push_back, pop_back, contains - may traverse the entire list
# S:
#   O(1) for all methods
#   O(n) for the data structure overall

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self._size = 0
    
    def size(self):
        return self._size
    
    def push_front(self, val):
        new = Node(val)
        new.next = self.head
        self.head = new
        self._size += 1

    def pop_front(self):
        if not self.head:
            return None
        val = self.head.val
        self.head = self.head.next
        self._size -= 1
        return val

    def push_back(self, val):
        new = Node(val)
        if not self.head:
            self.head = new
        else:
            curr = self.head
            while curr.next: # Traverse to the last node
                curr = curr.next
            curr.next = new
        self._size += 1

    def pop_back(self):
        if not self.head:
            return None
        if not self.head.next: # Single node - remove it
            val = self.head.val
            self.head = None
            self._size -= 1
            return val
        curr = self.head # Traverse to the second-to-last node
        while curr.next and curr.next.next:
            curr = curr.next
        val = curr.next.val # Save the last node's value
        curr.next = None # Detach the last node
        self._size -= 1
        return val

    def contains(self, val):
        curr = self.head
        while curr:
            if curr.val == val:
                return curr
            curr = curr.next
        return None
    

    
# # Singly Linked List Design

# Implement a `SinglyLinkedList` class with the following methods:

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
# list = SinglyLinkedList()
# list.push_front(1)  # List is now: 1
# list.push_front(2)  # List is now: 2->1
# list.push_back(3)   # List is now: 2->1->3
# list.contains(2)    # Returns node with value 2
# list.contains(4)    # Returns None (value not found)
# list.size()         # Returns 3
# list.pop_front()    # Returns 2, list is now: 1->3
# list.pop_back()     # Returns 3, list is now: 1

# Example 2:
# list = SinglyLinkedList()
# list.pop_front()    # Returns None (empty list)
# list.pop_back()     # Returns None (empty list)
# list.size()         # Returns 0

# This diagram shows the typical structure of a singly linked list:

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/singly-linked-list-design-1.png

# Constraints:

# - You have to create the `Node` class with a `val` field and a `next` pointer. If your language is typed, you can either make the type of `val` be generic or integer.
# - The `push_front()`, `pop_front()`, and `size()` methods should take `O(1)` time if the elements are integers.
# - The list can contain up to `10^5` nodes.