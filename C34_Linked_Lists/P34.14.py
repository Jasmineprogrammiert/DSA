# Problem 34.14 - Linked List Block Reversal
# Given the head of a singly linked list and a number k > 0, reverse blocks of
# k nodes. If the last block has size less than k, do not reverse it.
#
# Example 1:
# head = 1 -> 2 -> 3 -> 4 -> null, k = 2
# Output: 2 -> 1 -> 4 -> 3 -> null
#
# Example 2:
# head = 1 -> 2 -> 3 -> 4 -> 5 -> null, k = 3
# Output: 3 -> 2 -> 1 -> 4 -> 5 -> null
#
# Example 3:
# head = 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null, k = 2
# Output: 2 -> 1 -> 4 -> 3 -> 6 -> 5 -> null
#
# Constraints:
# - Create Node class with integer val field and next pointer
# - Up to 10^5 nodes