# ————— Problem —————

# Given a pointer to a specific node in a tree, node, that might be null, and might or might not be the root, implement the following functions:
# a. Return whether it is a leaf
# b. Return the values of its children as an array of length at most 2
# c. Return the values of its grandchildren as an array of length at most 4
# d. Return the size of the node's subtree. A node's subtree includes itself and all of its descendants
# e. Return the height of its subtree


# ————— Solution —————

# a/b/c: T: O(1), S: O(1)
# d/e: T: O(n), S: O(h) — where n = subtree nodes and h = subtree height (call stack)

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_leaf(node):
    if not node:
        return False
    return not node.left and not node.right

def children_values(node):
    if not node:
        return []
    values = []
    if node.left:
        values.append(node.left.val)
    if node.right:
        values.append(node.right.val)
    return values

def grandchildren_values(node):
    if not node:
        return []
    values = []
    for child in [node.left, node.right]:
        if child and child.left:
            values.append(child.left.val)
        if child and child.right:
            values.append(child.right.val)
    return values

def subtree_size(node):
    if not node:
        return 0
    left_size = subtree_size(node.left)
    right_size = subtree_size(node.right)
    return left_size + right_size + 1

def subtree_height(node):
    if not node:
        return 0
    left_height = subtree_height(node.left)
    right_height = subtree_height(node.right)
    return max(left_height, right_height) + 1 # +1 for 'node'