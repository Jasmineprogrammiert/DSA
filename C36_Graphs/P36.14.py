# Problem 36.14 - Multi-Exit Maze
# Given a grid maze of letters: 'X' = wall, 'O' = exit, '.' = walkable.
# Return a grid where each cell has the min steps to the closest exit.
# Walls return -1. Every walkable cell can reach an exit.
#
# Example 1:
# maze = ["...X.O","OX.X..","...X..",".X....","XOX.XX"]
# Output:
# [[ 1, 2, 3,-1, 1, 0],
#  [ 0,-1, 4,-1, 2, 1],
#  [ 1, 2, 3,-1, 3, 2],
#  [ 2,-1, 4, 5, 4, 3],
#  [-1, 0,-1, 6,-1,-1]]
#
# Example 2:
# maze = ["...",".O.","..."]
# Output: [[2,1,2],[1,0,1],[2,1,2]]
#
# Constraints:
# - 1 <= maze.length, maze[i].length <= 1000