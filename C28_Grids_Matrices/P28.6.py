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