# Problem 35.2 - Hidden Message
# Each node has a text field with exactly two characters. The first character is
# 'b', 'i', or 'a'. The second character is part of the hidden message.
# Decode order:
# - 'b': node goes before its left subtree, left subtree before right subtree
# - 'a': node goes after its right subtree, right subtree after left subtree
# - 'i': node goes after its left subtree and before its right subtree
# Return the hidden message as a string.
#
# Example:
#                  bn
#                /    \
#              i_      a!
#             /  \     /
#           ae    it  br
#          /  \         \
#        bi    bc        ay
#
# Output: "nice_try!"
#
# Constraints:
# - Node class has left, right, and text fields
# - Number of nodes <= 10^5
# - Height <= 500
# - text is length 2: first char is 'b'/'i'/'a', second is a letter or number