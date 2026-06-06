# ————— Problem —————

# If the problem asks us to find the node's parent instead of its children, we would be stuck: in the standard node type, there is no way to go up the tree. Consider an alternative definition of the node class that also includes a pointer to the parent:

# class Node:
#     def __init__(self, id, parent, left, right):
#         self.id = id # a unique integer id
#         self.parent = parent
#         self.left = left
#         self.right = right

# Given a non-null node in the tree, node, which might or might not be the root, implement the following functions:
#
# a. Return whether it is the root.
# b. Return the IDs of all of its ancestors as an array, in any order.
# c. Return the depth of the node.
#
# d. Given two non-null nodes from the same tree, node1 and node2, return the ID of their lowest common ancestor. The lowest common ancestor or LCA of two nodes is the deepest node in the tree which is a non-strict ancestor of both. Non-strict means that a node is considered its own ancestor. For instance, in Figure 4, LCA(j, f) = f.
#
# e. Given two non-null nodes from the same tree, return the distance between them. The sequence of edges between two nodes is called a path, and the number of edges in the path is the distance between the two nodes. Note that, in a binary tree, the path between any two nodes is unique.
#
# Figure 4:          Depth
#         a            0
#        / \
#       b   c          1
#      / \   \
#     d   e   f        2
#    / \     / \
#   h   i   j   k      3
#
# LCA(h, e) = b    dist(h, e) = 3
# LCA(j, f) = f    dist(j, f) = 1
#
# Figure 5:
#           a
#          / \
#        b     c
#      2/ \3    \
#      d   e     f
#    1/ \      1/ \
#    h   i    j   k
#
# dist(h, e) = 3    dist(j, f) = 1


# ————— Solution —————
class Node:
    def __init__(self, id, parent, left, right):
        self.id = id # a unique integer id
        self.parent = parent
        self.left = left
        self.right = right

# The root is the only node without a parent:
def is_root(node):
    return not node.parent

# To find the ancestors and the depth of a node, we can traverse parent pointers up to the root either recursively or iteratively

# Iterative
def ancestor_ids(node):
    ids = []
    while node.parent:
        node = node.parent
        ids.append(node.id)
    return ids

def depth(node):
    res = 0
    while node.parent:
        node = node.parent
        res += 1
    return res

# Recursive
def ancestor_ids_rec(node):
    if not node.parent:
        return []
    return [node.parent.id] + ancestor_ids_rec(node.parent)

def depth_rec(node):
    if not node.parent:
        return 0
    return 1 + depth_rec(node.parent)

# The lowest-common ancestor (LCA) is the point in the two nodes' lists of non-strict ancestors (counting each node as its own ancestor) where the IDs start to match. They must match at some point, as all the nodes share at least one non-strict ancestor, the root.

# We can find the LCA using O(1) space using a two-pointer-style solution:
# 1. Keep a 'pointer' starting on each Node
# 2. Find the depth of the two nodes. If one of the pointers is deeper than the other, we 'catch up' its pointer to the height of the other
# 3. After both pointers are at the same depth, we check, depth by depth, if their ancestor at that depth is the same

def LCA(node1, node2):
    depth1 = depth(node1)
    depth2 = depth(node2)
    while depth1 > depth2:
        node1 = node1.parent
        depth1 -= 1
    while depth2 > depth1:
        node2 = node2.parent
        depth2 -= 1
    while node1.id != node2.id:
        node1 = node1.parent
        node2 = node2.parent
    return node1.id

# To go from node1 to node2, you must go up to their LCA, then back down to the other node.
# So distance = (edges from node1 up to LCA) + (edges from node2 up to LCA).
def distance(node1, node2):
    lca_id = LCA(node1, node2)
    dist = 0
    while node1.id != lca_id:  # walk node1 up to LCA, counting edges
        dist += 1
        node1 = node1.parent
    while node2.id != lca_id:  # walk node2 up to LCA, counting edges
        dist += 1
        node2 = node2.parent
    return dist