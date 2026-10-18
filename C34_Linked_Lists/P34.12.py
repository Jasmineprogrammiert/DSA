#           0    1    2                   IDX

#           1 -> 3 -> 5 -> None           HEAD1
#                     c1   nxt1
#           2 -> 4 -> 6 -> None           HEAD2
#                     c2   nxt2

#           1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
#                                    HERE

# Merge them IN PLACE by alternating one node from each, starting with `head1`
# Append any remaining elements to the end
# Return the new head

# m, n: number of nodes in the two lists
# T: O(min(m, n)) - interleave until one list ends; leftovers stay linked
# S: O(1) - rewire existing nodes using a fixed number of pointers

def linked_list_zip(head1, head2):
    if not head1 or not head2:
        return head1 or head2

    c1 = head1
    c2 = head2

    while c1 and c2:
        nxt1, nxt2 = c1.next, c2.next
        c1.next = c2
        if nxt1:
            c2.next = nxt1
        c1, c2 = nxt1, nxt2
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