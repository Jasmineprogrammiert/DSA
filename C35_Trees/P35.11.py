# Problem 35.11 - Most Protected Node
# Given the root of a non-empty binary tree, return the highest protection
# level of any node. The protection level is the minimum of four values:
# - Number of ancestors
# - Length of the longest chain of descendants
# - Number of nodes on the same level to its left
# - Number of nodes on the same level to its right
#
# Example:
#             O
#          /     \
#         O       O
#        / \     / \
#       O   O   O   O
#      / \   \   \   \
#     O   O   O   O   O
#    / \   \   \   \   \
#   O   O   O   O   O   O
#  /   / \     / \   \   \
# O   O   O   O   O   O   O
#
# Output: 2
# Protection levels:
#             0
#          /     \
#         0       0
#        / \     / \
#       0   1   1   0
#      / \   \   \   \
#     0   1   2   1   0
#    / \   \   \   \   \
#   0   1   0   1   1   0
#  /   / \     / \   \   \
# 0   0   0   0   0   0   0
#
# Constraints:
# - Number of nodes <= 10^5
# - Height <= 500
# - Node values don't matter