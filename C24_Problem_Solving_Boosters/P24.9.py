# sort by date -> "earlier" is free, only ads left to compare
# exactly one above me == hi > ads[i] > hi2
#
# for i sorted by date:
#     if hi > ads[i] > hi2: keep i
#     fold ads[i] into hi / hi2      <- test BEFORE folding

# n: number of launches
# T: O(n log n) — the sort dominates, the sweep itself is O(n)
# S: O(n) — the sorted index order


# # Company Launches

# A VC firm is analyzing `n` companies that launched in 1992. We are given two arrays of length `n`, `launches` and `ads`. The `i`-th company launched on day `launches[i]` (which is a number between 1 and 366) and had an ad spending of `ads[i]` (in dollars). We say a launch overshadows another launch if:

# 1. It happened earlier
# 2. It had more ad spending

# Find the indices (starting at `0`) of all the launches that were overshadowed by exactly one other launch. You can assume that all dates are different and all ad spendings are different.

# Example:
# dates = [12, 5, 2, 11, 4, 8, 3, 1, 10]
# ads   = [11, 4, 2,  5, 9, 7, 6, 3,  1]
# Indices:  0  1  2   3  4  5  6  7   8
# Output: [2, 5]
# Explanation:
# launch 2 is only overshadowed by launch 7
# launch 5 is only overshadowed by launch 4

# Constraints:

# - `0 <= n <= 10^5` where `n` is the length of both arrays
# - `1 <= launches[i] <= 366` (day in 1992, which has 366 days)
# - `1 <= ads[i] <= 10^9` (ad spending in dollars)
# - All launch dates are different
# - All ad spending amounts are different