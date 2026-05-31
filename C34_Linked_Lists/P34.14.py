class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Reverse every k-length block in-place; skip last block if < k nodes
# DS: Dummy node + prev pointer (same as "Dummy, Walk, Break, Flip, Reattach")
# Steps:
#   1. Probe: walk k steps from curr — if we hit None, return (block too short)
#   2. Save: tail = walk k-1 from curr, after = tail.next
#   3. Break: prev.next = None, tail.next = None
#   4. Flip: reverse(curr) → new_head
#   5. Reattach: prev.next = new_head, curr.next = after
#   6. Advance: prev = curr, curr = after — repeat
# Edge cases: k = 1 (no change), k > list length (no change), exact multiple of k.
#
# n: number of nodes
# T: O(n) — each node visited at most twice (probe + reverse)
# S: O(1) — only pointer rewiring, no extra storage
        
def block_reversal(head, k):
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    curr = head
    
    while curr:
        # Step 1: Check if k nodes remain
        check = curr
        for _ in range(k):
            if not check:
                return dummy.next
            check = check.next
        
        # Step 2: Reverse k-length block
        # Save pointers
        tail = curr
        for _ in range(k - 1):
            tail = tail.next
        after = tail.next
        
        # Break  
        prev.next = None
        tail.next = None
        
        # Flip (save, flip, advance)
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
        
        # Advance for next block
        prev = curr
        curr = after
        
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