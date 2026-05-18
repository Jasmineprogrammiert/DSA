# Problem 36.15 - RGB Distances
# Given a grid of 'R', 'G', 'B' characters, return a grid where:
# - R cells: taxicab distance to closest G
# - G cells: taxicab distance to closest B
# - B cells: taxicab distance to closest R
# Taxicab distance = abs(r1-r2) + abs(c1-c2)
# Guaranteed at least one of each color.
#
# Example 1:
# screen = ["RRRGRB","BGRGRR","RRRGRR","RGRRRR","GBGRGG"]
# Output:
# [[2,1,1,2,1,1],
#  [1,1,1,3,1,2],
#  [2,1,1,4,1,2],
#  [1,1,1,1,1,1],
#  [1,2,1,1,3,4]]
#
# Example 2: screen = ["RGB"] -> [[1,1,2]]
#
# Constraints:
# - 1 <= rows, cols <= 1000
# - At least one of each color