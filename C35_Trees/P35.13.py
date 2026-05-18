# Problem 35.13 - BST Nearest Value
# Given the root of a non-empty BST and a target value, find the closest value
# to target in the tree. Tie: return the smaller value.
#
# Example 1:
#               5
#             /    \
#            2      9
#             \    / \
#              4  9   11
#                  \
#                   9
# target = 4 -> 4
#
# Example 2: same tree, target = 3 -> 2
#
# Constraints:
# - 1 <= number of nodes <= 10^4
# - -10^9 <= node.val <= 10^9
# - -10^9 <= target <= 10^9
# - The tree is a valid BST