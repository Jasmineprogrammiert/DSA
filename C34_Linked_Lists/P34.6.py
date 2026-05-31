# Reverse a singly linked list in place
#
# "Save, Flip, Advance" — repeat until curr is None
#   1. Save:    nxt = curr.next        (remember what's next)
#   2. Flip:    curr.next = prev       (point arrow backward)
#   3. Advance: prev = curr, curr = nxt (move both forward)
#
# Return prev (the new head)
#
# Edge cases: empty list or single node — already reversed
#
# n = number of nodes
# T: O(n) - each node is visited once
# S: O(1) - only three pointer variables

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
def linked_list_reversal(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

# # Build list: 1 -> 2 -> 3 -> None
# a = Node(1)
# b = Node(2)
# c = Node(3)
# a.next = b
# b.next = c

# # Reverse it
# new_head = linked_list_reversal(a)

# # Print the reversed list
# curr = new_head
# while curr:
#     print(curr.val, end=" -> ")
#     curr = curr.next
# print("None")



# # Linked-List Reversal

# Given the head, `head`, of a singly linked list, reverse the nodes **in place** and return the new head of the list. The list may be empty.

# Example 1:
# Input: 1 -> 2 -> 3 -> null
# Output: 3 -> 2 -> 1 -> null

# Example 2:
# Input: null
# Output: null

# Example 3:
# Input: 1 -> null
# Output: 1 -> null

# Constraints:

# - You have to create the `Node` class with an integer `val` field and a `next` pointer.
# - The list can contain up to `10^5` nodes.