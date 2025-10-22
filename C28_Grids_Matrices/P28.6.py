# Initialize a new grid filled by 0 with the same size as the original
# Iterate over each cell [r, c] in the original grid,
# scan the subgrid from [r, c] to [R-1, C-1]
    # track the max value in this subgrid
# Assign the max value to new_grid[r][c]
# Return the filled new_grid
# T: O(R*C)^2

# More efficient way with dynamic programming:
# Processing the grid from bottom-right to top-left, so that
# each cell's subgrid max can be reused in other computations
# For each cell (r, c), the max in the subgrid from (r, c) to (R-1, C-1) is:
    # The max of:
    # grid[r][c]
    # The cell to the right: new_grid[r][r+1] (if exists)
    # The cell below: new_grid[r+1][c] (if exists)
    # The cell disgonally down-right: new_grid[r+1][c+1] (if exists)
# So new_grid is filled from bottom-right to top-left

# T: O(R*C)
# O: O(R*C)

def subgrid_max(grid):
    R, C = len(grid), len(grid[0])
    new_grid = [[0] * C for _ in range(R)]
    
    for r in range(R):
        for c in range(C):
            max_cell = -float('inf')
            for subgrid_r in range(r, R):
                for subgrid_c in range(c, C):
                    if grid[subgrid_r][subgrid_c] > max_cell:
                        max_cell = grid[subgrid_r][subgrid_c]
            new_grid[r][c] = max_cell     
            
    return new_grid



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