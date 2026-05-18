# Problem 35.12 - BST Search
# A BST is a binary tree where for every node:
# - All values in its left subtree are <= the node's value
# - All values in its right subtree are >= the node's value
# Given the root and a target value, return true if the tree contains the target.
#
# Example 1:
#               5
#             /    \
#            2      9
#             \    / \
#              4  9   11
#                  \
#                   9
# target = 4 -> True
#
# Example 2: same tree, target = 3 -> False
#
# Constraints:
# - Number of nodes <= 10^5
# - Node values between 0 and 10^9