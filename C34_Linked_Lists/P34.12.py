# Problem 34.12 - Linked-List Zip
# Given the heads of two singly linked lists, merge them by alternating one node
# from each, starting with head1. If lists are not the same size, append remaining
# elements to the end. Modify in place without creating new nodes. Return the new head.
#
# Example 1:
# head1 = 1 -> 3 -> 5 -> null
# head2 = 2 -> 4 -> 6 -> null
# Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
#
# Example 2:
# head1 = 1 -> 2 -> 3 -> 4 -> null
# head2 = 8 -> 7 -> null
# Output: 1 -> 8 -> 2 -> 7 -> 3 -> 4 -> null
#
# Example 3:
# head1 = null, head2 = null
# Output: null
#
# Constraints:
# - Create Node class with integer val field and next pointer
# - Up to 10^5 nodes