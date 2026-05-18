# Problem 35.7 - Evaluate Expression Tree
# Given the root of an N-ary tree representing an arithmetic expression.
# Node has three fields: kind, num, children.
# - kind = "num": Number node, value is in num field
# - kind = "sum"/"product"/"max"/"min": Operation node, applies to children
#
# Evaluate the tree:
# - Number node: return its num field
# - Operation node: apply the operation to all children's values
#
# Example:
#      min
#     /   \
#  max     +
#  /|\      \
# 4 6 +      *
#    / \    / \
#   5   7  6   8
# Output: 12
#
# Constraints:
# - Number of nodes <= 10^5
# - Height <= 500
# - Number node values between -10^4 and 10^4
# - Evaluation at every node between -10^4 and 10^4