# Problem 34.7 - Sublist Reversal
# Given the head of a singly linked list, and two indices left and right with
# 0 <= left < right, reverse all nodes between the two indices in place and
# return the new head.
# - If left is beyond the last index, do not modify the list.
# - If only right is beyond the last index, reverse everything up to the last node.
#
# Example 1:
# head = 1 -> 2 -> 3 -> 4 -> 5 -> null, left = 1, right = 3
# Output: 1 -> 4 -> 3 -> 2 -> 5 -> null
#
# Example 2:
# head = 1 -> 2 -> 3 -> 4 -> 5 -> null, left = 2, right = 7
# Output: 1 -> 2 -> 5 -> 4 -> 3 -> null
#
# Example 3:
# head = 1 -> 2 -> null, left = 5, right = 6
# Output: 1 -> 2 -> null
#
# Constraints:
# - Create Node class with integer val field and next pointer
# - Up to 10^5 nodes