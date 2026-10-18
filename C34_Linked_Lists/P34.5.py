#         1 -> 2 -> 3 -> None        ORG
#              curr_org
#    0 -> 1 -> 2 -> None             COPY
#    dummy     curr_new

# n: number of nodes
# T: O(n) - visit each original node once
# S: O(n) - create n copied nodes; auxiliary space is O(1)
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def linked_list_copy(head):
    dummy = Node(0)
    curr_org = head
    curr_new = dummy

    while curr_org:
        curr_new.next = Node(curr_org.val)
        curr_org = curr_org.next
        curr_new = curr_new.next
    return dummy.next


# # Linked-List Copy

# Given the head, `head`, of a singly linked list, return a new list with the same values. The list may be empty.

# Example 1:
# Input: 1 -> 2 -> 3 -> null
# Output: 1 -> 2 -> 3 -> null

# Example 2:
# Input: null
# Output: null

# Example 3:
# Input: 1 -> null
# Output: 1 -> null

# Constraints:

# - You have to create the `Node` class with an integer `val` field and a `next` pointer.
# - The list can contain up to `10^5` nodes.