# Create a n*n grid initialized with 0
# Fill from the end (n-1, n-1) instead of center (easier to turn direction)
# with the highest value n*n - 1
# Defind four directions: up, left, donw, right
    # [[-1, 0], [0, -1], [1, 0], [0, 1]]
# Use a loop that decrements the highest val to 0
# Track current location grid[r][c] and direction index dir

# Before filling, check if the next cell is valid (not out of bound and unfilled)
# Turns clockwise by (i + 1) % n 
# Move to the next cell:
    # new_r = r + directions[dir][0]
    # new_l = l + directions[dir][1]

# n: length of grid
# T: O(n^2) - (n^n - 1) iterations
# S: O(n^2) - a new grid with size n^n is created


# (i + 1) % n returns the next index in a circular sequence of length n, wrapping back to 0 after reaching n - 1. This is commonly used to cycle through elements in arrays where the end wraps around beginning

def Spiral_Order(n):
    def is_valid(grid, r, c):
        return 0 <= r < len(grid) and 0 <= c < len(grid) and grid[r][c] == 0
    
    grid = [[0] * n for _ in range(n)]
    val = n * n - 1
    r = c = n - 1
    directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    dir = 0
    
    while val > 0:
        grid[r][c] = val
        val -= 1
        if not is_valid(grid, r + directions[dir][0], c + directions[dir][1]):
            dir = (dir + 1) % 4
        r, c = r + directions[dir][0], c + directions[dir][1]
    return grid



# # Spiral Order

# Given a positive and odd integer `n`, return an `nxn` grid of integers filled as follows: the grid should have every number from `0` to `n^2 - 1` in _spiral order_, starting by going down from the center and turning clockwise.

# Example 1:
# n = 5
# Output: [[16, 17, 18, 19, 20],
#          [15,  4,  5,  6, 21],
#          [14,  3,  0,  7, 22],
#          [13,  2,  1,  8, 23],
#          [12, 11, 10,  9, 24]]

# Example 2:
# n = 1
# Output: [[0]]

# Example 3:
# n = 3
# Output: [[4, 5, 6],
#          [3, 0, 7],
#          [2, 1, 8]]

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/spiral-order-1.png

# Constraints:

# - `0 < n < 1000`
# - `n` is odd