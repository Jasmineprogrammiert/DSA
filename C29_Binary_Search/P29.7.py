# try to find the position of the target in a 2D grid, otherwise return [-1, -1]
# to flatten out the 2D array, imagine it's a flat array
# can binary search the array withotu creating one:
    # l, r = 0, R * C - 1
    # R, C = len(grid), len(grid[0]) 
# To find the target's position in the 2D array: 
    # row, col = i // C, i % C
# If any target is found, 
# it will be the first element in the "after" section

# traisition_point_recipe:
    # is_before() when grid[row][col] < target
    # l, r = 0, R*C-1
    # row = i // C
    # col = i % C
    # handle three edge cases:
        # 1. the range is empty (not applicable)
        # 2. l is after
        # 3. r is before
    
    # where l and r are not next to each other (r - l > 1)
#        mid = (l + r) // 2
#        if is_before(mid):
#            l = mid
#        else:
#            r = mid
#    return l (last 'before'), r (first 'after'), or something else,
#    depending on the problem

# n: R * C
# T: O(log n) - binary search
# O: O(1)

def search_in_sorted_grid(grid, target):
    R, C = len(grid), len(grid[0])

    def is_before(i):
        row, col = i // C, i % C
        return grid[row][col] < target
    
    if grid[0][0] > target or grid[R-1][C-1] < target:
         return [-1, -1]
    
    l, r = 0, R*C - 1
    while r - l > 1:
        mid = (l + r) // 2
        if is_before(mid):
            l = mid
        else:
            r = mid

    # r is the first element that is NOT < target
    row, col = r // C, r % C
    if grid[row][col] == target:
        return [row, col]
    return [-1, -1]
# print(search_in_sorted_grid([[1, 2, 4, 5],
#         [6, 7, 8, 9]], 4))



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