# Problem 35.1 - Aligned Chain
# Given a binary tree, a node is aligned if its value equals its depth (distance
# from root). A descendant chain is a sequence of nodes where each is the parent
# of the next. Return the length of the longest descendant chain of aligned nodes.
# The chain does not need to start at the root.
#
# Example:
#                 7
#                / \
#               1   3
#              / \   \
#             2   8   2
#            / \     / \
#           4   3   3   3
#
# Output: 3
# Aligned nodes: 1 (depth 1), 2 (depth 2), 3 (depth 3)
# Longest chain: 1 -> 2 -> 3 on the left subtree
#
# Constraints:
# - Number of nodes <= 10^5
# - Height <= 500
# - Node values between 0 and 10^9