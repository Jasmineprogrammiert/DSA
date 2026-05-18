# Problem 35.9 - Most Prolific Level
# Given the root of a binary tree, return the most prolific level. The
# prolificness of a level is the average number of children over all nodes
# in that level. Return -1 if the tree is empty. Tie: return any.
#
# Example:
#       O
#      /
#     O
#    / \
#   O   O
#  / \   \
# O   O   O
#
# Output: 1
# Level 0: prolificness 1
# Level 1: prolificness 2
# Level 2: prolificness 1.5
# Level 3: prolificness 0
#
# Constraints:
# - Number of nodes <= 10^5
# - Node values don't matter