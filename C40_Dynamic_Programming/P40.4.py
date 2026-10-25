# dp[r][c]: number of valid paths reaching (r, c)
# dp[2][2] = up + left + diagonal = 2 + 3 + 2 = 7

# GRID          DP
# 0 1 1         1 0 0
# 0 0 0         1 2 2
# 1 0 0         0 3 7

# R: number of rows, C: number of columns
# T: O(R * C) - visit each cell once, O(1) work per cell
# S: O(R * C) - the dp table stores one path count per cell

def count_paths(grid):
    R, C = len(grid), len(grid[0])
    dp = [[0] * C for _ in range(R)]
    
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 1:
                continue
            if r == 0 and c == 0:
                dp[r][c] = 1
                continue
            if r > 0:
                dp[r][c] += dp[r-1][c]
            if c > 0:
                dp[r][c] += dp[r][c-1]
            if r > 0 and c > 0:
                dp[r][c] += dp[r-1][c-1]
    
    return dp[R-1][C-1]


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