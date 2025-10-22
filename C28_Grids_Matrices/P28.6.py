# Solution 28.6
# Ch 28: Grids & Matrices
# page 322
# Line 7 is
# res[r][c] = max(res[r][c], grid[r + 1][c])
# but it should be
# res[r][c] = max(res[r][c], res[r + 1][c])
# The same applies to line 9.

# Ch 28: Grids & Matrices
# page 323
# The bottom left cell in "A+B" should sum to 16



# # Subgrid Maximums

# Given a rectangular `RxC` grid of integers, `grid`, with `R > 0` and `C > 0`, return a new grid with the same dimensions where each cell `[r, c]` contains the maximum in the subgrid with `[r, c]` in the top-left corner and `[R-1, C-1]` in the bottom-right corner.

# Example 1:
# grid =  [[1, 5, 3],
#          [4,-1, 0],
#          [2, 0, 2]]
# Output: [[5, 5, 3],
#          [4, 2, 2],
#          [2, 2, 2]]

# Example 2:
# grid =  [[5]]
# Output: [[5]]
# Explanation: For a 1x1 grid, each cell's subgrid is just itself.

# Example 3:
# grid =  [[1, 2, 3]]
# Output: [[3, 3, 3]]
# Explanation: For a single row, each cell's subgrid includes all elements to its right.

# Constraints:

# - 1 ≤ R, C ≤ 10^3
# - -10^4 ≤ grid[i][j] ≤ 10^4