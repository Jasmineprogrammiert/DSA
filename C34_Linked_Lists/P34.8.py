# Problem 34.8 - Linked-List Cycle Detection
# Given the head of a singly linked list that may or may not contain a cycle,
# return whether the list has a cycle. A cycle happens when the next pointer of
# a node points to a node already in the list. Assume at least one node.
#
# Example 1:
# 1 -> 2 -> 3
#      ^    |
#      \----/
# Output: True
#
# Example 2:
# 1 -> 2 -> 3 -> null
# Output: False
#
# Example 3:
# 1 -> 2 ---\
#      ^    |
#      \----/
# Output: True
#
# Follow-up: Can you do it using only O(1) extra space?
#
# Constraints:
# - Create Node class with integer val field and next pointer
# - 1 <= nodes <= 10^5