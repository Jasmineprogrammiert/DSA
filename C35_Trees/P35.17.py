# Problem 35.17 - BST Merge Into Array
# Given the roots of two BSTs, return an array containing all elements from
# both trees in sorted order. The trees may contain duplicate values.
#
# Example 1:
# root1:
#               5
#             /    \
#            2      9
#             \    / \
#              4  9   11
# root2:
#               3
#             /    \
#            2      7
#           /      / \
#          1      6   8
# Output: [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 9, 11]
#
# Example 2:
# root1:       root2:
#     2            2
#    / \          / \
#   2   2        2   2
# Output: [2, 2, 2, 2, 2, 2]
#
# Constraints:
# - Number of nodes per tree <= 10^5
# - Height per tree <= 500
# - Node values between 0 and 10^9