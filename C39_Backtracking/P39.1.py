# DECISION TREE
#   NODE=(cell (r,c), running sum) | BRANCH=down / right | PRUNE=out of bounds X
#   LEAF=reach bottom-right (R-1,C-1) -> OK   ACTION=keep the MAX sum
#
# grid = [[1, 4],
#         [2, 7]]   start (0,0), goal (1,1)
#
#                 (0,0) sum=1
#           down |           \ right
#         (1,0) sum=3      (0,1) sum=5
#             | right          | down
#         (1,1) sum=10     (1,1) sum=12
#            OK               OK
#             \_____ max _____/
#                   = 12
#
# BAD method: O(b^d * A)
#   b = branching factor: 2
#   d = depth of the call tree: R + C - 2 — moves to goal: down R-1, right C-1
#   A = additional (non-recursive) work per node: O(1)
# 
# R: number of rows in the grid
# C: number of columns in the grid
# T: O(2^(R + C - 2))
# S: O(R + C) — call stack, O(1) extra work per call
#   deepest live path: R + C - 1 cells (start + R+C-2 moves)

def max_sum_path(grid):
    R, C = len(grid), len(grid[0])
    max_sum = float("-inf")
    
    def visit(r, c, cur_sum):
        nonlocal max_sum
        if r == R - 1 and c == C - 1:
            max_sum = max(max_sum, cur_sum)
            return
        if r+1 < R:
            visit(r+1, c, cur_sum + grid[r+1][c]) # Go down
        if c+1 < C:
            visit(r, c+1, cur_sum + grid[r][c+1]) # Go right
    visit(0, 0, grid[0][0])
    return max_sum


# # Max-Sum Path

# Given a non-empty grid of positive integers, `grid`, find the path from the top-left corner to the bottom-right corner with the largest sum. You can only go down or to the right (not diagonal).

# Example 1: grid = [[1, 4, 3],
#                    [2, 7, 6],
#                    [5, 8, 9]]
# Output: 29. The maximum path is 1 -> 4 -> 7 -> 8 -> 9.

# Example 2: grid = [[5]]
# Output: 5

# Example 3: grid = [[1, 2, 3]]
# Output: 6. The maximum path is 1 -> 2 -> 3.

# Constraints:

# - `1 <= R, C <= 1000`, where `R` is the number of rows and `C` is the number of columns in the grid.
# - `1 <= grid[i][j] <= 1000`.