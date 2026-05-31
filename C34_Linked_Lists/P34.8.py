# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None

# Use slow and fast pointers, the former advances one node at a time, whereas the later advances two nodes.
#   If they meet, there's a cycle.
#   If the faster one reaches None, there isn't a cycle
# 
# n: number of nodes
# T: O(n) — fast closes the gap by 1 each step, so they meet within one cycle
# S: O(1) — only two pointers

def has_cycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# # Example 1: 1 -> 2 -> 3 -> back to 2 (cycle)
# a = Node(1); b = Node(2); c = Node(3)
# a.next = b; b.next = c; c.next = b
# print(has_cycle(a))  # True



# # Linked-List Cycle Detection

# You are given the head of a singly linked list, `head`, that may or may not contain a cycle. A _cycle_ happens when the `next` pointer of a node is a node that is already in the linked list. Return whether the list has a cycle. Assume the list has at least one node.

# Example 1:
# Input: 1 -> 2 -> 3
#             ^    |
#             \----/

# Output: True

# Example 2:
# Input: 1 -> 2 -> 3 -> null

# Output: False

# Example 3:
# Input: 1 -> 2 ---\
#             ^    |
#             \----/

# Output: True

# Follow-up: Can you do it using only `O(1)` extra space?

# Constraints:

# - You have to create the `Node` class with an integer `val` field and a `next` pointer.
# - The list contains at least `1` node and at most `10^5` nodes.