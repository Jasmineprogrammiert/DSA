# 4-Directional Max-Sum Path -- backtracking (self-avoiding walk)
# Grid is <= 5x5, so brute-forcing every path IS the intended solution:
# 4-way moves + no-revisit make the visited-set part of the state -> no clean DP exists.
#
# State : (r, c) = where I am; path_sum = sum collected so far; visited = cells on THIS path.
# Child : the 4 neighbors via (dr, dc) = up / down / left / right.
# Prune : skip a neighbor that is off-grid OR already visited.
# Leaf  : reached bottom-right (R-1, C-1) -> record max_sum, then stop.
# Work  : max_sum = max(max_sum, path_sum); seed it at -inf so all-negative grids work.
#
# Backtrack: add to visited BEFORE recursing, remove AFTER -- the remove is what frees a cell so a DIFFERENT path can reuse it later.
#
# R: number of rows in grid
# C: number of columns in grid
# T: O(3^(R*C)) — ≤3 new dirs per cell (one is where you came from), depth ≤ R*C
# S: O(R*C) — call stack + visited set

def max_sum_path(grid):
    DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    R, C = len(grid), len(grid[0])
    max_sum = float("-inf")
    visited = set()

    def visit(r, c, path_sum):
        nonlocal max_sum
        if (r, c) == (R - 1, C - 1):
            max_sum = max(max_sum, path_sum)
            return
        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in visited:
                visited.add((nr, nc))
                visit(nr, nc, path_sum + grid[nr][nc])
                visited.remove((nr, nc))

    visited.add((0, 0))
    visit(0, 0, grid[0][0])
    return max_sum


# # 4-Directional Max-Sum Path

# Given an `RxC` grid of integers (which can be negative), `grid`, find the path from the top-left corner to the bottom-right corner with the largest sum and return its sum. You can go in all four directions (diagonals not allowed), but you **can't visit a cell more than once**.

# Example: grid = [[ 1, -4,  3],
#                  [-2,  7, -6],
#                  [ 5, -4,  9]]
# Output: 12
# The maximum path is 1 -> -4 -> 7 -> -2 -> 5 -> -4 -> 9, which has sum 12.

# Constraints:

# - `grid` has at least `1` to `5` rows and `1` to `5` columns.
# - `grid[i][j]` is an integer between `-100` and `100`.