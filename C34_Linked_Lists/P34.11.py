# Problem 34.11 - Remove Kth Node From the End
# Given the head of a singly linked list and a number k, remove the k-th node
# from the end of the list. Assume k <= list size.
#
# Example 1:
# head = 1 -> 2 -> 3 -> 4 -> null, k = 2
# Output: 1 -> 2 -> 4 -> null
#
# Example 2:
# head = 1 -> 2 -> 3 -> 4 -> null, k = 4
# Output: 2 -> 3 -> 4 -> null
#
# Example 3:
# head = 1 -> null, k = 1
# Output: null
#
# Follow-up: Can you do it without computing the length of the list first?
#
# Constraints:
# - Create Node class with integer val field and next pointer
# - 1 <= nodes <= 10^5
# - 1 <= k <= n