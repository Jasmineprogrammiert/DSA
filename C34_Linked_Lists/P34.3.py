# Problem 34.3 - Linked-List-Based Stack
# Implement a Stack class using a singly linked list.
#
# push(v): Adds a value v at the top of the stack.
# pop(): Removes and returns the value at the top. Returns None if empty.
# peek(): Returns the value at the top without removing it. Returns None if empty.
# size(): Returns the number of elements in the stack.
# empty(): Returns True if the stack is empty, False otherwise.
#
# Example 1:
# stack = Stack()
# stack.push(1)   # 1
# stack.push(2)   # 1->2
# stack.push(3)   # 1->2->3
# stack.peek()    # Returns 3
# stack.size()    # Returns 3
# stack.empty()   # Returns False
# stack.pop()     # Returns 3, stack: 2->1
# stack.pop()     # Returns 2, stack: 1
# stack.pop()     # Returns 1, stack empty
# stack.empty()   # Returns True
#
# Example 2:
# stack = Stack()
# stack.pop()     # Returns None
# stack.peek()    # Returns None
# stack.size()    # Returns 0
# stack.empty()   # Returns True
#
# Constraints:
# - All methods should be O(1)
# - Up to 10^5 elements
# - Do not use a dynamic array. Implement the linked list from scratch.