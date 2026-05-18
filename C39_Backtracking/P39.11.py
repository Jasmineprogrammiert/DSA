# Problem 39.11 - Escape with All Clues
# Grid with 0 (walkable), 1 (obstacle), 2 (clue). Start at (0,0).
# Find shortest path collecting all clues without repeating cells.
# Return the path or [] if impossible. At least one clue exists.
#
# Example 1:
# room = [[0,1,0],[0,2,0],[0,0,2]]
# Output: [[0,0],[1,0],[1,1],[1,2],[2,2]]
#
# Example 2:
# room = [[0,0,0],[2,1,2]] -> [] (can't get both without revisiting)
#
# Example 3:
# room = [[0,0,1,2],[0,1,0,0]] -> [] (can't reach clue)
#
# Constraints:
# - 1 to 6 rows, 1 to 6 columns
# - room[0][0] is 0
# - At least one 2