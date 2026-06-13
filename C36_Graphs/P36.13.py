# Goal: how many 4-directionally connected land regions (islands)?
# DFS flood-fill - an island is a connected component of land cells
#   - scan every cell in reading order
#   - unvisited land -> new island, count += 1, then flood it
#   - flood: mark visited, recurse into valid neighbors
#   - is_valid: in bounds, not visited, is land (grid[r][c] == 1)
# Edge cases: empty grid [] or [[]] -> 0
#
# n: R * C (total cells)
# T: O(n) - each cell visited once; visited set blocks repeats
# S: O(n) - visited set + recursion stack (island <= 500 caps depth)

def count_islands(grid):
    if not grid or not grid[0]:
        return 0

    R, C = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    visited = set()
    count = 0

    def is_valid(r, c):
        return (0 <= r < R and
                0 <= c < C and
                (r, c) not in visited and
                grid[r][c] == 1)

    def visit(r, c):
        visited.add((r, c))
        for dir_r, dir_c in directions:
            nbr_r, nbr_c = r + dir_r, c + dir_c
            if is_valid(nbr_r, nbr_c):
                visit(nbr_r, nbr_c)

    for r in range(R):
        for c in range(C):
            if is_valid(r, c):
                visit(r, c)
                count += 1

    return count


# # Count Grid Islands

# In this classic problem, you are given a binary grid, `grid`, where `0` represents water and `1` represents solid ground. The goal is to count the number of _islands_ in the grid, where an island is a four-directionally contiguous land region.

# Return the number of islands in the grid.

# Example 1: grid = [
#   [0, 0, 1, 0],
#   [1, 1, 0, 1],
#   [0, 0, 1, 1]
# ]
# Output: 3

# Example 2: grid = [
#   []
# ]
# Output: 0

# Example 3: grid = [
#   [1]
# ]
# Output: 1

# Example 4: grid = [
#   [1, 0, 1],
#   [0, 0, 0],
#   [1, 0, 1]
# ]
# Output: 4

# Constraints:

# - `0 <= grid.length <= 1000`
# - `0 <= grid[i].length <= 1000`
# - `grid[i][j]` is either `0` or `1`
# - All the rows have the same length
# - Each island contains at most `500` cells