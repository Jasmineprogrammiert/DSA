class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# n: number of nodes in the stack
# T: O(1) - all operations are on the head
# S:
#   O(1) for all methods
#   O(n) for the data structure overall

class Stack: # LIFO: push/pop/peek all at the head
    def __init__(self):
        self.head = None
        self._size = 0
    
    def size(self):
        return self._size
    
    def push(self, val):
        new = Node(val)
        new.next = self.head
        self.head = new
        self._size += 1

    def pop(self):
        if not self.head:
            return None
        val = self.head.val
        self.head = self.head.next
        self._size -= 1
        return val

    def peek(self):
        if not self.head: 
            return None
        return self.head.val
    
    def empty(self):
        return self._size == 0



# # Linked-List-Based Stack

# Implement a `Stack` class using a singly linked list.

# It should support the following methods:

# push(v):
#     Adds a value v at the top of the stack.

# pop():
#     Removes the value at the top of the stack and returns its value.
#     If the stack is empty, returns None.

# peek():
#     Returns the value at the top of the stack without removing it.
#     If the stack is empty, returns None.

# size():
#     Returns the number of elements in the stack.

# empty():
#     Returns True if the stack is empty, False otherwise.

# Examples:

# Example 1:
# stack = Stack()
# stack.push(1)    # Stack is now: 1
# stack.push(2)    # Stack is now: 1->2
# stack.push(3)    # Stack is now: 1->2->3
# stack.peek()     # Returns 3
# stack.size()     # Returns 3
# stack.empty()    # Returns False
# stack.pop()      # Returns 3, stack is now: 2->1
# stack.pop()      # Returns 2, stack is now: 1
# stack.pop()      # Returns 1, stack is now empty
# stack.empty()    # Returns True

# Example 2:
# stack = Stack()
# stack.pop()      # Returns None (empty stack)
# stack.peek()     # Returns None (empty stack)
# stack.size()     # Returns 0
# stack.empty()    # Returns True

# Constraints:

# - If your language is typed, you can either make the type of the stack elements generic, or use integers.
# - All the methods should take `O(1)` time if the elements are integers.
# - The stack can contain up to `10^5` elements.
# - Do not use a dynamic array. You have to implement the linked list from scratch.