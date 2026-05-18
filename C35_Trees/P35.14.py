# Problem 35.14 - BST Validation
# Given the root of a binary tree, determine if it is a valid BST.
# A BST: for every node, all left subtree values <= node value, all right >= node value.
#
# Example 1:
#               5
#             /    \
#            2      9
#             \    / \
#              4  9   11
#                  \
#                   9
# Output: True
#
# Example 2:
#               5
#             /    \
#            2      12
#             \    / \
#              4  10  13
#                  \
#                   9
# Output: False
#
# Constraints:
# - Number of nodes <= 10^5
# - Height <= 500
# - Node values between 0 and 10^9