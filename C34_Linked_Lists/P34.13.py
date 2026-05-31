# DS: Singly linked list
# Approach: Single pointer. Since list is sorted, duplicates are adjacent.
#   Compare cur.val with cur.next.val:
#     - If equal: skip the duplicate (cur.next = cur.next.next)
#     - If not equal: advance cur (cur = cur.next)
# Edge cases: empty list, all duplicates, no duplicates
#
# n: number of nodes
# T: O(n) — single pass through the list
# S: O(1) — only pointer rewiring, no extra storage

def remove_duplicates(head):
    cur = head
    while cur and cur.next:
        if cur.val == cur.next.val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head



# # Duplicate Removal In Sorted Linked List

# Given the head of a singly linked list with **sorted** integer values, `head`, remove duplicates **in place**.

# Example 1:
# head = 1 -> 1 -> 1 -> 3 -> 5 -> 5 -> null
# Output: 1 -> 3 -> 5 -> null

# Example 2:
# head = 1 -> 1 -> 1 -> 1 -> 1 -> null
# Output: 1 -> null

# Example 3:
# head = null
# Output: null

# Constraints:

# - You have to create the `Node` class with an integer `val` field and a `next` pointer.
# - The list can contain up to `10^5` nodes.