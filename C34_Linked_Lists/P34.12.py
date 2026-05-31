# DS: two pointers (cur1, cur2) tracking position in each list
# Steps:
#   1. save next1 and next2 before rewiring
#   2. cur1.next = cur2, cur2.next = next1 (if exists)
#   3. advance both pointers to saved nexts
#   4. repeat until one list runs out
# Edge: null head → return the other
# 
# n: number of nodes in list1
# m: number of nodes in list2
# T: O(min(n,m)) — stops when the shorter list runs out
# S: O(1) — rewires existing nodes in place

def merge(head1, head2):
    if not head1 or not head2:
        return head1 or head2

    cur1 = head1
    cur2 = head2

    while cur1 and cur2:
        next1 = cur1.next
        next2 = cur2.next

        cur1.next = cur2
        if next1:
            cur2.next = next1
        cur1 = next1
        cur2 = next2
    return head1



# # Linked-List Zip

# Given the heads of two singly linked lists, `head1` and `head2`, merge them together by alternating one node from each, starting with `head1`. If lists are not the same size, append any remaining elements to the end. Modify the lists **in place** without creating new nodes. Return the new head.

# Example 1:
# head1 = 1 -> 3 -> 5 -> null
# head2 = 2 -> 4 -> 6 -> null
# Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null

# Example 2:
# head1 = 1 -> 2 -> 3 -> 4 -> null
# head2 = 8 -> 7 -> null
# Output: 1 -> 8 -> 2 -> 7 -> 3 -> 4 -> null

# Example 3:
# head1 = null
# head2 = null
# Output: null

# Constraints:

# - You have to create the `Node` class with an integer `val` field and a `next` pointer.
# - The lists can contain up to `10^5` nodes.