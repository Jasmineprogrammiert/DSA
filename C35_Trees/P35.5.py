# Problem 35.5 - Triangle Count
# Given the root of a binary tree, return the number of triangles.
# A triangle is a set of three distinct nodes a, b, c where:
# - a is the lowest common ancestor of b and c
# - b and c have the same depth
# - the path from a to b only consists of left children
# - the path from a to c only consists of right children
# (nodes in these paths can have children on the other side)
#
# Example 1:
#          0
#      /       \
#     1         2
#      \       / \
#       3     4   5
#      / \   /     \
#     6   7 8       9
# Output: 4
# Triangles: (0,1,2), (3,6,7), (2,4,5), (2,8,9)
#
# Example 2:
#       0
#    /      \
#   1        4
#  /  \       \
# 2    3       5
# Output: 3
# Triangles: (0,1,4), (1,2,3), (0,2,5)
#
# Constraints:
# - Number of nodes <= 10^5
# - Height <= 500
# - Node values don't matter