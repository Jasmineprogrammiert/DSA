# bottom-up (tabulation): count down/right/diag paths all 0 -> path sum stays 0
#   dp[r][c] = number of all-0 paths reaching (r, c)
#   grid[r][c] == 1 -> dp = 0 (blocked);  start (0, 0) if 0 -> dp = 1
#   else dp[r][c] = up + left + diag (in-bounds predecessors)
# answer = dp[R-1][C-1]
#
# R: number of rows in the grid
# C: number of columns in the grid
# Subproblems: R*C — one per cell (r, c)
# Non-recursive work: O(1) — sum of 3 fixed neighbors
# T: O(R * C) — R*C subproblems * O(1) work
# S: O(R * C) — the dp table (squeezable to O(C) by keeping 2 rows)

def count_zero_sum_path(grid):
    R, C = len(grid), len(grid[0])
    dp = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 1:
                continue
            if r == c and c == 0:
                dp[r][c] = 1
                continue
            total = 0
            if r > 0:
                total += dp[r-1][c]
            if c > 0:
                total += dp[r][c-1]
            if r > 0 and c > 0:
                total += dp[r-1][c-1]
            dp[r][c] = total
    return dp[R-1][C-1]

# top-down (memoization): num_paths(r, c) = # all-0 paths from (r, c) to exit
#   out of bounds or blocked (grid == 1) -> 0;  reached exit (R-1, C-1) -> 1
#   else num_paths = down (r+1, c) + right (r, c+1) + diag (r+1, c+1)
# answer = num_paths(0, 0)
# caveat: stack depth up to (R-1)+(C-1) ~ 2000 > default recursion limit of
#         1000 -> RecursionError on large grids (bottom-up above has no stack)
#
# R: number of rows in the grid
# C: number of columns in the grid
# Subproblems: R*C — one per cell (r, c)
# Non-recursive work: O(1) — sum of 3 fixed moves
# T: O(R * C) — R*C subproblems * O(1) work
# S: O(R * C) — memo up to R*C entries + recursion stack (depth up to R + C)

def count_zero_sum_path_memo(grid):
    R, C = len(grid), len(grid[0])
    memo = {}

    def num_paths(r, c):
        if r >= R or c >= C or grid[r][c] == 1:
            return 0
        if (r, c) in memo:
            return memo[(r, c)]
        if r == R - 1 and c == C - 1:
            return 1
        memo[(r, c)] = (num_paths(r + 1, c)
                        + num_paths(r, c + 1)
                        + num_paths(r + 1, c + 1))
        return memo[(r, c)]

    return num_paths(0, 0)


# # Count 0-Sum Paths

# Given a non-empty `RxC` binary grid, `grid`, return the number of paths from the top-left corner to the bottom-right corner with a sum of `0`. You can only go down, to the right, or diagonally down and to the right.

# Example 1:
# grid = [
#   [0, 1, 1],
#   [0, 0, 0],
#   [1, 0, 0]
# ]
# Output: 7

# Example 2:
# grid = [
#   [1]
# ]
# Output: 0

# Example 3:
# grid = [
#   [0, 0],
#   [0, 0]
# ]
# Output: 3

# The figure below illustrates the possible paths for Example 1:

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/count-0-sum-paths-1.png

# Constraints:

# - `R` is at least `1` and at most `1000`.
# - `C` is at least `1` and at most `1000`.
# - Each element in the grid is either `0` or `1`.