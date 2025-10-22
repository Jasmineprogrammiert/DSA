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