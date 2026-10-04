# 1 2       GRID
# 3 4

# 0 6       RES
# 7 4

# 2         R
# 2         C
# 0         r
# 1         c

# for r in range(1, -1, -1):
#     for c in range(1, -1, -1):

# Start bottom-right: below and right sums are ready; subtract their diagonal overlap
# R, C: number of rows and columns
# T: O(R * C) - one visit per cell, O(1) work each
# S: O(R * C) - output grid; O(1) auxiliary space

def subgrid_sums(grid):
    R, C = len(grid), len(grid[0])
    res = [row.copy() for row in grid]

    for r in range(R - 1, -1, -1):
        for c in range(C - 1, -1, -1):
            if r + 1 < R:
                res[r][c] += res[r + 1][c]
            if c + 1 < C:
                res[r][c] += res[r][c + 1]
            if r + 1 < R and c + 1 < C:
                res[r][c] -= res[r + 1][c + 1]
    return res


# # Subgrid Sums

# Given a rectangular `RxC` grid of integers, `grid`, with `R > 0` and `C > 0`, return a new grid with the same dimensions where each cell `[r, c]` contains the sum of all the elements in the subgrid with `[r, c]` in the top-left corner and `[R - 1, C - 1]` in the bottom-right corner.

# Example 1:
# grid =  [[-1,  2,  3],
#          [ 4,  0,  0],
#          [-2,  0,  9]]
# Output: [[15, 14, 12],
#          [11,  9,  9],
#          [ 7,  9,  9]]

# Example 2:
# grid =  [[5]]
# Output: [[5]]
# Explanation: For a 1x1 grid, each cell's subgrid is just itself.

# Example 3:
# grid =  [[1, 2, 3]]
# Output: [[6, 5, 3]]
# Explanation: For a single row, each cell's subgrid includes all elements to its right.

# Constraints:

# - 1 ≤ R, C ≤ 10^3
# - -10^3 ≤ grid[i][j] ≤ 10^3