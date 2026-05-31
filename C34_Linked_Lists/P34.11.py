class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# DS: slow/fast pointers with dummy node
# Steps:
#   1. dummy before head — so removing head isn't a special case
#   2. advance fast k steps to open a gap
#   3. move both until fast reaches end → slow is at prev of target
#   4. slow.next = slow.next.next (skip the target)
# Edge: removing head → dummy handles it
# 
# n: number of nodes
# T: O(n) — single pass through the list
# S: O(1) — only pointer variables

def remove_kth_node(head, k):
    dummy = Node(0)
    dummy.next = head
    
    fast = dummy.next
    for _ in range(k):
        fast = fast.next
    
    slow = dummy
    while fast:
        slow = slow.next
        fast = fast.next
    
    slow.next = slow.next.next
    
    return dummy.next



# # Remove Kth Node From The End

# Given the head of a singly linked list, `head`, and a number `k`, remove the `k`-th node **from the end** of the list. Assume `k` is smaller than or equal to the list's size.

# Example 1:
# head = 1 -> 2 -> 3 -> 4 -> null
# k = 2

# Output: 1 -> 2 -> 4 -> null

# Example 2:
# head = 1 -> 2 -> 3 -> 4 -> null
# k = 4

# Output: 2 -> 3 -> 4 -> null

# Example 3:
# head = 1 -> null
# k = 1

# Output: null

# Follow-up: Can you do it without computing the length of the list first?

# Constraints:

# - You have to create the `Node` class with an integer `val` field and a `next` pointer.
# - The list contains at least `1` node and at most `10^5` nodes.
# - `1 <= k <= n`, where `n` is the number of nodes in the list.