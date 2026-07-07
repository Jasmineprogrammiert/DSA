# Solution state: `subset` is the current subset at each node in the decision tree;
#   `i` is the next element for which we must make a decision.
# Child creation: modify the parent's `subset` in place. After appending S[i] and
#   recursing, cleanup (popping S[i]) restores the state for the sibling branch.
# Pruning: not possible — both children (pick / skip) must be visited.
# Leaf processing: append a COPY of `subset` to the global result. Must be a copy,
#   or later pops would mutate the subset we already stored.
# Additional work: O(1) at internal nodes, O(n) at each leaf to copy `subset` —
#   nothing left to optimize for this problem.
#
# Universal backtracking template:
#   def visit(partial_solution):
#       if full_solution(partial_solution):
#           # process leaf / full solution
#       else:
#           for choice in choices(partial_solution):
#               # prune children where possible
#               child = apply_choice(partial_solution)
#               visit(child)
#   visit(empty_solution)
#
# For each element decide OUT (skip) or IN (take) -> binary tree of depth n, each leaf a subset
#                 START  subset=[]
#                /               \
#           a OUT               a IN
#             /                    \
#        subset=[]             subset=[a]
#         /     \               /      \
#     b OUT   b IN          b OUT     b IN
#       /       \            /          \
#     []        [b]        [a]        [a,b]   <- save each leaf
#
# n: length of S
# T: O(n * 2^n) — 2^n leaves, and copying each subset costs O(n)
# S: O(n) auxiliary — recursion stack + subset, both depth n (excludes O(n * 2^n) output)

def subset_enumeration(S):
    res = []
    subset = []
    def visit(i):
        if i == len(S):
            res.append(subset.copy())
            return
        subset.append(S[i])  # Choice 1: pick S[i]
        visit(i + 1)
        subset.pop()         # Cleanup: un-choose
        visit(i + 1)         # Choice 2: skip S[i]
    visit(0)
    return res


# # Subset Enumeration

# Given a set of elements, `S`, a subset of `S` is another set obtained by removing any number of elements from `S` (including none or all of them). As usual with sets, order does not matter.

# Given an array of unique characters, `S`, return all possible subsets in any order.

# Example: S = ['x', 'y', 'z']
# Output: [[],
#          ['x'],
#          ['y'],
#          ['z'],
#          ['x', 'y'],
#          ['x', 'z'],
#          ['y', 'z'],
#          ['x', 'y', 'z']]

# Constraints:

# - The elements in `S` are unique.
# - The length of `S` is at most 12.