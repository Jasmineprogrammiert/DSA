# Problem 35.4 - Tree Layout
# Given the root of a non-empty binary tree, lay out the tree on a grid:
# - Root at (r, c) = (0, 0)
# - Left subtree: increase r by 1
# - Right subtree: increase c by 1
#
# Two nodes are stacked if they share the same (r, c) coordinates.
# Return the maximum number of nodes stacked on the same coordinate.
#
# Example:
#          1
#        /   \
#      2       3
#    /  \     /
#   4    5   6
#    \      / \
#     7    8   9
#
# Output: 2
# Layout:
# 1 -- 3
# |    |
# 2 - 5,6 - 9
# |    |
# 4 - 7,8
# Most stacked: 5,6 or 7,8
#
# Constraints:
# - Number of nodes <= 10^5
# - Height <= 500
# - Node values don't matter