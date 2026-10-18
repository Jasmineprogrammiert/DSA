# k = 2
#           D    0    1    2    3                  IDX
#           0 -> 2 -> 1 -> 3 -> 4 -> null          ORG
#                     HEAD                         GIVEN
#                     prev
#                          curr
#                          check
#                tail

#                2 -> 1 -> 4 -> 3 -> null                  OUTPUT

# REVERSED       REMAINING
# None           1 -> 2 -> None
# p              c    nxt

# 1 -> None      2 -> None
# p              c

# 2 -> 1 -> None
# p              c = None

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# n: number of nodes
# T: O(n) - each node is checked, located and reversed a constant number of times
# S: O(1) - rewire existing nodes using a fixed number of pointers and one dummy node

def block_reversal(head, k):
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    curr = head

    while curr:
        check = curr
        for _ in range(k):
            if check is None:
                return dummy.next
            check = check.next

        tail = curr
        for _ in range(k - 1):
            tail = tail.next

        prev.next = tail.next = None

        p, c = None, curr
        while c:
            nxt = c.next
            c.next = p
            p = c
            c = nxt

        prev.next = p
        curr.next = check

        prev = curr
        curr = check
    return dummy.next


# # Linked-List Block Reversal

# Given the head of a singly linked list, `head`, and a number `k > 0`, reverse blocks of `k` nodes of the linked list. If the last block has size less than `k`, do not reverse it.

# Example 1:
# head = 1 -> 2 -> 3 -> 4 -> null
# k = 2

# Output: 2 -> 1 -> 4 -> 3 -> null

# Example 2:
# head = 1 -> 2 -> 3 -> 4 -> 5 -> null
# k = 3

# Output: 3 -> 2 -> 1 -> 4 -> 5 -> null

# Example 3:
# head = 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
# k = 2

# Output: 2 -> 1 -> 4 -> 3 -> 6 -> 5 -> null

# Constraints:

# - You have to create the `Node` class with an integer `val` field and a `next` pointer.
# - The list can contain up to `10^5` nodes.