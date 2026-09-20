# laminal arrays = the tree of halves, down to single elements
# each call returns (best, total) for its piece arr[l:r], half-open: l in, r out
#   total = left total + right total, no walking
#   best  = max(left best, right best, total)
# base case: one element, best and total are both arr[l]

# 0  1   2  3  4   5  6  7   8     IDX
# 3, -9, 2, 4, -1, 5, 5, -4        ARR
# l
#                            r     one past the end
#             mid

# n: length of arr
# T: O(n) - BAD: b = 2, d = log n, A = O(1), so 2^(log n) x 1 = n
# S: O(log n) - the call stack, one frame per halving

def laminal_arr(arr):
    def visit(l, r):
        if r - l == 1:
            return arr[l], arr[l]
        mid = (l + r) // 2
        l_best, l_total = visit(l, mid)
        r_best, r_total = visit(mid, r)
        total = l_total + r_total
        best = max(l_best, r_best, total)
        return best, total
    return visit(0, len(arr))[0]


# # Laminal Arrays

# We are given an array, `arr`, whose **length is a power of 2**.

# We define the set of _laminal arrays_ as follows:

# - The array `arr` is laminal.
# - Each half of a laminal array with even length is laminal.

# Find the laminal array with maximum sum and return its sum.

# Example 1: arr = [3, -9, 2, 4, -1, 5, 5, -4]
# Output: 6
# The laminal arrays are:
# [3, -9, 2, 4, -1, 5, 5, -4],
# [3, -9, 2, 4], [-1, 5, 5, -4],
# [3, -9], [2, 4], [-1, 5], [5, -4],
# [3], [-9], [2], [4], [-1], [5], [5], [-4]
# The one with the maximum sum is [2, 4].

# Example 2: arr = [1]
# Output: 1

# Example 3: arr = [-1, -2]
# Output: -1

# Example 4: arr = [1, 2, 3, 4]
# Output: 10

# Example 5: arr = [-2, -1, -4, -3]
# Output: -1

# Constraints:

# - The length of `arr` is a power of `2`
# - `1 ≤ len(arr) ≤ 10^5`
# - `-10^9 ≤ arr[i] ≤ 10^9`