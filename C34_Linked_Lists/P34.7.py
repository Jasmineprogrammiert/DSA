# Sublist Reversal — two methods
#
# Setup (both methods):
#   1. dummy -> head
#   2. Walk prev to node right before curr
#   3. If prev falls off the list, return early
#
# Method A: "Dummy, Walk, Break, Flip, Reattach"
#   4. curr = first node to reverse, tail = last node to reverse
#      after = tail.next
#   5. Break: prev.next = None, tail.next = None
#   6. Flip: reverse(curr) using "Save, Flip, Advance" → new_head
#   7. Reattach: prev.next = new_head, curr.next = after
#
# Method B: "Pluck and Insert" (in-place, more concise)
#   4. Loop (r - l) times: take node after curr, stick it after prev
#      - curr.next = next_node.next     (skip over)
#      - next_node.next = prev.next     (point to front)
#      - prev.next = next_node          (attach after prev)
#   Note: prev and curr NEVER move. Only next_node changes.
# 
# n: r - l (length of the sublist to reverse)
# T: O(n) - every node in the sublist visited once
# S: O(1) - reversed in-place using a fixed number of pointers

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# --- Method A: Break, Flip, Reattach ---
def sublist_reversal_a(head, l, r):
    dummy = Node(0)
    dummy.next = head
    prev = dummy

    for i in range(l):
        if not prev.next:
            return dummy.next
        prev = prev.next

    # Break
    curr = prev.next
    tail = curr
    for i in range(r - l):
        if not tail.next:
            break
        tail = tail.next
    after = tail.next
    prev.next = None
    tail.next = None

    # Flip (Save, Flip, Advance)
    p = None
    c = curr
    while c:
        nxt = c.next
        c.next = p
        p = c
        c = nxt

    # Reattach
    prev.next = p
    curr.next = after

    return dummy.next

# --- Method B: Pluck and Insert (in-place) ---
def sublist_reversal_b(head, l, r):
    dummy = Node(0)
    dummy.next = head
    prev = dummy

    for i in range(l):
        if not prev.next:
            return dummy.next
        prev = prev.next
    curr = prev.next

    for i in range(r - l):
        if not curr.next:
            break
        next_node = curr.next
        curr.next = next_node.next
        next_node.next = prev.next
        prev.next = next_node

    return dummy.next



# # Sublist Reversal

# Given the head, `head`, of a singly linked list, and two indices, `left` and `right`, with `0 ≤ left < right`, reverse all nodes between the two indices **in place** and return the new head of the list.

# If `left` is beyond the last index, do not modify the list. If only `right` is beyond the last index, reverse everything up to the last node.

# Example 1:
# head = 1 -> 2 -> 3 -> 4 -> 5 -> null
# left = 1
# right = 3

# Output: 1 -> 4 -> 3 -> 2 -> 5 -> null
# The first node (index 0) and the last node (index 4) stay the same

# Example 2:
# head = 1 -> 2 -> 3 -> 4 -> 5 -> null
# left = 2
# right = 7

# Output: 1 -> 2 -> 5 -> 4 -> 3 -> null
# All nodes starting at index 2 are reversed because index 7 is beyond
# the last index

# Example 3:
# head = 1 -> 2 -> null
# left = 5
# right = 6

# Output: 1 -> 2 -> null
# left is out of bounds, so we leave the list untouched

# Constraints:

# - You have to create the `Node` class with an integer `val` field and a `next` pointer.
# - The list can contain up to `10^5` nodes.