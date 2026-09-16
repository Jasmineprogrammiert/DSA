# target = 4

# 0 1 2 3 4 5 6 7   IDX
# 1 2 4 5 6 7 8 9   GRID
#   l
#     r

# flat index i <-> cell: row = i // C, col = i % C
# is_before(i): value at i < target -> r ends on the first value not below target, where target sits if it exists

# n: number of cells, R * C
# T: O(log n) - one binary search over the flattened grid; each probe is an O(1) cell read
# S: O(1) - a fixed number of variables regardless of the grid size

def search_in_sorted_grid(grid, target):
    R, C = len(grid), len(grid[0])

    def is_before(i):
        return grid[i // C][i % C] < target

    l, r = 0, R * C - 1
    if not is_before(l):
        return [0, 0] if grid[0][0] == target else [-1, -1]
    if is_before(r):
        return [-1, -1]

    while r - l > 1:
        mid = (l + r) // 2
        if is_before(mid):
            l = mid
        else:
            r = mid

    row, col = r // C, r % C
    return [row, col] if grid[row][col] == target else [-1, -1]


# # Search in Sorted Grid

# You are given a 2D grid of integers, `grid`, where each row is sorted (without duplicates), and the last value in each row is smaller than the first value in the following row. You are also given a target value, `target`. If the target is in the grid, return an array with its row and column indices. Otherwise, return `[-1, -1]`.

# Example 1:
# target = 4
# grid = [[1, 2, 4, 5],
#         [6, 7, 8, 9]]
# Output: [0, 2]. The number 4`` is found in row 0 and column 2.

# Example 2:
# target = 3
# grid = [[1, 2, 4, 5],
#         [6, 7, 8, 9]]
# Output: [-1, -1].

# Constraints:

# - `1 ≤ grid.length, grid[i].length ≤ 10000`
# - `-10^4 ≤ grid[i][j], target ≤ 10^4`
# - The grid has no duplicates