# Problem 35.3 - Aligned Path
# Given a binary tree, a node is aligned if its value equals its depth (distance
# from root). Return the length of the longest path of aligned nodes. A path can
# start and end at any node.
#
# Example:
#                 7
#                / \
#               1   4
#              / \   \
#             2   8   2
#            / \     / \
#           4   3   3   3
#
# Output: 3
# Aligned nodes: 1, 2, 3 (left subtree) and 2, 3, 3 (right subtree)
# Two paths of length 3: 1->2->3 (left) and 3->2->3 (right)
#
# Constraints:
# - Number of nodes <= 10^5
# - Height <= 500
# - Node values between 0 and 10^9