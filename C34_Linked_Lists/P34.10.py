class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Slow/fast pointers (one pass)
# 1. slow moves 1 step, fast moves 2 steps
# 2. When fast hits the end, slow is at the middle (it covered half the distance)
# 3. No length count needed; lands on the right-middle for even n
# 
# n: number of nodes
# T: O(n) — each node visited once by fast pointer
# S: O(1) — only two pointers

def middle_val(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.val

# Brute-force (two passes)
# 1. Count nodes -> length n
# 2. Walk n // 2 steps
# 3. Return that node's val (n // 2 lands on the right-middle for even n)

def middle_val(head):
    n = 0
    node = head
    while node:
        n += 1
        node = node.next

    node = head
    for _ in range(n // 2):
        node = node.next
    return node.val



# # Linked-List Midpoint

# Given the head of a non-empty singly linked list, `head`, return the value in the middle of the linked list. If there is an even number of nodes, return the value of the right middle node.

# Example 1:
# Input: 10 -> 20 -> 30 -> null
# Output: 20

# Example 2:
# Input: 10 -> 20 -> 30 -> 40 -> null
# Output: 30

# Example 3:
# Input: 10 -> null
# Output: 10

# Follow-up: Can you do it without computing the length of the list first?

# Constraints:

# - You have to create the `Node` class with an integer `val` field and a `next` pointer.
# - The list contains at least `1` node and at most `10^5` nodes.