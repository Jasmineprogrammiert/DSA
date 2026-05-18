# Problem 39.10 - 4-Directional Max-Sum Path
# Given an RxC grid of integers (can be negative), find the path from
# top-left to bottom-right with largest sum. Can go all 4 directions
# (no diagonals), can't revisit cells.
#
# Example:
# grid = [[1,-4,3],[-2,7,-6],[5,-4,9]] -> 12
# Path: 1 -> -4 -> 7 -> -2 -> 5 -> -4 -> 9
#
# Constraints:
# - 1 to 5 rows, 1 to 5 columns
# - -100 <= grid[i][j] <= 100