# Approach A — swap in place, index as divider
# ============================================================================
# Trick: keep every element in one array `perm`; index `i` splits it into prefix `perm[:i]`
#   (placed) and pool `perm[i:]` (still to place). The divider IS the bookkeeping.
# State: `perm` + `i` (the slot we're deciding).
# Choice: for each j in the pool (i..n-1) swap perm[i], perm[j] to place a candidate in slot i,
#   recurse on i+1, then swap back to restore the pool. Looping from `i` freezes the prefix,
#   so no element is reused.
# Leaf: at i == n-1 the last element is forced -> prefix is a full permutation; append a COPY.
# Mantra: place a pool element in slot i -> trust visit(i+1) -> swap back -> next j.
#                       visit(0)  [ | a b c ]
#            j=0 /           j=1 |           j=2 \
#         [a | b c]        [b | a c]        [c | b a]
#         j=1 / \ j=2      j=1 / \ j=2      j=1 / \ j=2
#       [ab|c] [ac|b]    [ba|c] [bc|a]    [cb|a] [ca|b]
#        abc    acb       bac    bca       cba    cab    <- append each leaf
#   (down an edge = swap(i, j); up = swap back)
#
# n: length of arr
# T: O(n * n!) — n! leaves, each permutation copied in O(n)
# S: O(n) auxiliary — recursion stack + `perm` (excludes output)

def permutations_swap(arr):
    if not arr:
        return [[]]
    res = []
    perm = arr.copy()

    def visit(i):
        if i == len(perm) - 1:
            res.append(perm.copy())
            return
        for j in range(i, len(perm)):
            perm[i], perm[j] = perm[j], perm[i]   # place
            visit(i + 1)
            perm[i], perm[j] = perm[j], perm[i]   # restore

    visit(0)
    return res


# ============================================================================
# Approach B — explicit `path` + `used[]`
# ============================================================================
# Trick: build the answer in a separate `path`; `used[]` marks taken elements so each level
#   only picks from those still unused.
# State: `path` (so far) + `used[]`.
# Choice: for each unused index k (`if used[k]: continue`), mark + append arr[k], recurse,
#   then undo BOTH — pop AND clear used[k] — so the sibling branch starts clean.
# Leaf: at len(path) == len(arr) all placed; append a COPY. (Empty input handled: 0 == 0.)
# Extends cleanly: duplicates -> sort + skip repeats; length k -> base case len(path) == k.
#                        START  path=[]
#             /               |               \
#          pick x           pick y           pick z
#          /   \            /   \            /   \
#      pick y pick z    pick x pick z    pick x pick y
#      [x,y,z][x,z,y]   [y,x,z][y,z,x]   [z,x,y][z,y,x]  <- save each leaf
#   (at each level try every UNUSED element)
#
# T: O(n * n!) — n! leaves, each path copied in O(n)
# S: O(n) auxiliary — recursion stack + path + used[] (excludes output)

def permutations_used(arr):
    res = []
    path = []
    used = [False] * len(arr)

    def visit():
        if len(path) == len(arr):
            res.append(path[:])
            return
        for k in range(len(arr)):
            if used[k]:
                continue
            used[k] = True
            path.append(arr[k])
            visit()
            path.pop()
            used[k] = False

    visit()
    return res


# # Permutation Enumeration

# A _permutation_ of a list is a list with the same elements but in any order. Finding all permutations means finding all possible orderings of the input elements.

# Given an array of unique characters, `arr`, return all possible permutations, in any order.

# Example 1: arr = ['x', 'y', 'z']
# Output: [['x', 'y', 'z'],
#          ['x', 'z', 'y'],
#          ['y', 'x', 'z'],
#          ['y', 'z', 'x'],
#          ['z', 'x', 'y'],
#          ['z', 'y', 'x']]

# Example 2: arr = ['x']
# Output: [['x']]

# Constraints:

# - The elements in `arr` are unique.
# - The length of `arr` is at most `10`.