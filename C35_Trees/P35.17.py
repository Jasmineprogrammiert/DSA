# Goal: return all elements of two BSTs merged in sorted order?
#   - inorder(tree) -> sorted list (BST inorder is non-decreasing)
#   - inorder both trees -> arr1, arr2, each already sorted
#   - merge arr1, arr2 with two pointers -> res
#       - arr1[p1] < arr2[p2] -> take arr1[p1]
#       - arr1[p1] > arr2[p2] -> take arr2[p2]
#       - equal -> take both
#   - drain leftovers of whichever list still has elements
#
# n: nodes in tree1, m: nodes in tree2
# T: O(n + m) - two linear inorder traversals + one linear merge pass
# S: O(n + m) - arr1, arr2, res hold all elements

def bst_merge(root1, root2):
    arr1, arr2, res = [], [], []
    p1, p2 = 0, 0

    def inorder(node, arr):
        if not node:
            return
        inorder(node.left, arr)
        arr.append(node.val)
        inorder(node.right, arr)

    inorder(root1, arr1)
    inorder(root2, arr2)

    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] < arr2[p2]:
            res.append(arr1[p1])
            p1 += 1
        elif arr1[p1] > arr2[p2]:
            res.append(arr2[p2])
            p2 += 1
        else:
            res.append(arr1[p1])
            res.append(arr2[p2])
            p1 += 1
            p2 += 1

    if p1 > len(arr1) - 1:
        res.extend(arr2[p2:])
    if p2 > len(arr2) - 1:
        res.extend(arr1[p1:])

    return res


# # BST Merge Into Array

# A binary search tree (BST) is a binary tree where, for _every_ node:

# - All the values on its **left** subtree are _less than or equal_ to the node's value.
# - All the values on its **right** subtree are _greater than or equal_ to the node's value.

# Given the roots of two binary search trees, return an array containing all elements from both trees in sorted order. The trees may contain duplicate values.

# Example:
# root1 =
#               5
#             /    \
#            2      9
#             \    / \
#              4  9   11
# root2 =
#               3
#             /    \
#            2      7
#           /      / \
#          1      6   8

# Output: [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 9, 11]

# Example 2:
# root1 =
#               2
#             /    \
#            2      2

# root2 =
#               2
#             /    \
#            2      2

# Output: [2, 2, 2, 2, 2, 2]

# Constraints:

# - The number of nodes of each tree is at most `10^5`
# - The height of each tree is at most `500`
# - The value at each node is between `0` and `10^9`