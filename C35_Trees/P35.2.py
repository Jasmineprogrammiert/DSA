# Tree DFS — 3 info flows:
#   Down   (param):  parent tells child   → e.g. depth, path sum
#   Up     (return): child tells parent   → e.g. subtree size, height
#   Global (state):  across branches      → e.g. max seen, result list
#
#   def visit(node, down_info):
#       if not node:
#           return up_info
#       left  = visit(node.left,  down_info)
#       right = visit(node.right, down_info)
#       global_state = ...          # side effect (across branches)
#       return up_info              # to parent

# Append char in order based on node's first char (b=before, i=in, a=after)
#   Down:   none
#   Up:     none
#   Global: message.append(char) — collect chars in traversal order
#
#   visit(node):
#     b: append, left, right
#     i: left, append, right
#     a: left, right, append
#
# n: number of nodes, h: height of tree
# T: O(n) - each node visited once
# S: O(h) - recursion

def hidden_message(root):
    message = []

    def visit(node):
        if not node:
            return
        if node.val[0] == 'b':
            message.append(node.val[1])
            visit(node.left)
            visit(node.right)
        elif node.val[0] == 'i':
            visit(node.left)
            message.append(node.val[1])
            visit(node.right)
        else:
            visit(node.left)
            visit(node.right)
            message.append(node.val[1])

    visit(root)
    return ''.join(message)

# Alt: string concat (pure up flow, no global state)
# + Cleaner, no nested helper
# - O(n²) due to immutable string concat in worst case
def hidden_message_v2(node):
    if not node:
        return ""
    first, second = node.val
    left = hidden_message_v2(node.left)
    right = hidden_message_v2(node.right)
    if first == 'b':
        return second + left + right
    elif first == 'a':
        return left + right + second
    return left + second + right


# # Hidden Message

# The self-proclaimed 'cryptography expert' in your friend group has devised their own schema to hide messages in binary trees. Each node has a text field with exactly two characters. The first character is either `'b'`, `'i'`, or `'a'`. The second character is part of the hidden message. To decode the message, you have to read the hidden-message characters in the following order:

# - If the first character in a node is `'b'`, the node goes before its left subtree, and the left subtree goes before the right subtree.
# - If it is `'a'`, the node goes after its right subtree, and the right subtree goes after the left subtree.
# - If it is `'i'`, the node goes after its left subtree and before its right subtree.

# Given the root of the binary tree, return the hidden message as a string.

# Example:

#                  bn
#                /    \
#              i_      a!
#             /  \     /
#           ae    it  br
#          /  \         \
#        bi    bc        ay

# Output: "nice_try!"

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/trees_fig10.png

# Constraints:

# - Assume we have a binary tree node class with a `left` and `right` fields, and a `text` field.
# - The number of nodes is at most `10^5`
# - The height of the tree is at most `500`
# - The text field is a string of length `2`. The first character is either `'b'`, `'i'`, or `'a'`. The second character is a letter or number.