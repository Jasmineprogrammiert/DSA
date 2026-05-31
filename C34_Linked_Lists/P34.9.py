# DS: list (brute force) or deque (optimal)

# Optimal — O(n) time, O(n) space, n = length of node
# 1. Walk prev → appendleft() each val
# 2. Walk next → append() each val

from collections import deque

def convert_to_array(node):
    res = deque([node.val])
    curr = node
    while curr.prev:
        curr = curr.prev
        res.appendleft(curr.val)
    curr = node
    while curr.next:
        curr = curr.next
        res.append(curr.val)
    return list(res)

# Brute force — O(n) time, O(n) space
# 1. Walk prev to find the head
# 2. Walk next from head, collect vals into list
def convert_to_array(node):
    curr = node
    while curr.prev:
        curr = curr.prev
    res = []
    while curr: 
        res.append(curr.val)
        curr = curr.next
    return res



# # Doubly Linked List To Array

# Given a non-null node, `node`, from a doubly linked list, which might or might not be the head, return an array with the values in the list, from head to tail.

# Example 1:
# head = null <-> 1 <-> 2 <-> 3 <-> 4 <-> null
# node = a pointer to the node at index 2

# Output: [1, 2, 3, 4]

# Example 2:
# head = null <-> 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> null
# node = a pointer to the node at index 0

# Output: [1, 2, 3, 4, 5]

# Constraints:

# - You have to create the `Node` class with an integer `val` field and `prev` and `next` pointers.
# - The list can contain up to `10^5` nodes.