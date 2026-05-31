class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Clarify: deep copy, list may be empty
# DS: two pointers to walk old and new lists in sync
# Steps: loop through old list, create + attach new nodes → return new head (head is the entry point to the full chain)
#   - Dummy node: create dummy → loop all nodes uniformly → return dummy.next (skip placeholder). No base case needed
#   - Without dummy: copy head first → loop remaining nodes → return new head. Needs if not head check
# Edge cases: empty list, single node (dummy handles empty naturally; without dummy needs explicit check)
#
# n: number of nodes in the list
# T: O(n) - traverse the entire list once, creating a new node each step
# S: O(n) - n new nodes created for the copied list

# Dummy Node
def dummy_copy_list(head):
    dummy = Node(0)
    curr_new = dummy
    curr_old = head
    while curr_old:
        curr_new.next = Node(curr_old.val)
        curr_new = curr_new.next
        curr_old = curr_old.next
    return dummy.next

def copy_list(head):
    if not head: 
        return None
    new_head = Node(head.val)
    curr_new = new_head
    curr_old = head.next
    while curr_old:
        curr_new.next = Node(curr_old.val) # attach new node to the list
        curr_new = curr_new.next # move pointer forward
        curr_old = curr_old.next
    return new_head



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