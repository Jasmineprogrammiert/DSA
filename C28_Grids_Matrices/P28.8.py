# Transposition: swaps element at (i, j) to (j, i)
# Clockwise rotation: the first row becomes the last column, the 2nd row becomes the second-last column etc.
    # 1. transpose; 2. reverse each row of the transposed matrix
# Anti-clockwise rotation: the last column becomes the first row, the 2nd column becomes the second-last row etc.
    # 1. transpose; 2. reverse the row order of the transposed matrix
# ...
# T: O(n^2)
# S: O(1)

class Matrix:
    def __init__(self, grid):
        self.grid = [row.copy() for row in grid]
    
    def transposition(self):
        grid = self.grid
        for r in range(len(grid)):
            for c in range(r):
                grid[r][c], grid[c][r] = grid[c][r], grid[r][c]
    
    def clockwise_rotation(self):
        self.transposition()
        self.horizontal_reflection()
    
    def anticlockwise_rotation(self):
        self.transposition()
        self.vertical_reflection()
        
    def horizontal_reflection(self):
        for row in self.grid:
            row.reverse()
        
    def vertical_reflection(self):
        self.grid.reverse()

# class Matrix:
#     def __init__(self, grid):
#         self.grid = grid
    
#     def transposition(self):
#         transposed = [list(row) for row in zip(*self.grid)]
#         return transposed
    
#     def clockwise_rotation(self):
#         transposed = self.transposition()
#         c_rotation = [row[::-1] for row in transposed]
#         return c_rotation
    
#     def anticlockwise_rotation(self):
#         transposed = self.transposition()
#         c_rotation = transposed[::-1]
#         return c_rotation
        
#     def horizontal_reflection(self):
#         reflected = [row[::-1] for row in self.grid]
#         return reflected
        
#     def vertical_reflection(self):
#         reflected = self.grid[::-1]
#         return reflected

# grid = [
#     [1, 2, 3], 
#     [4, 5, 6], 
#     [7, 8, 9]
# ]

# res = Matrix(grid).horizontal_reflection()
# print(res)



# # Matrix Operations

# Basic matrix operations sometimes come up in coding interviews because they involve interesting grid transformations, but they usually don't assume background knowledge.

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/matrix-operations-1.png

# - **Transposition**: The first row becomes the first column, the second row becomes the second column, and so on.
# - **Rotation**: A transformation that turns the matrix 90 degrees, clockwise or counterclockwise.
# - **Horizontal reflection**: The first column becomes the last column, the second column becomes the second last, and so on.
# - **Vertical reflection**: The first row becomes the last row, the second row becomes the second last, and so on.

# Implement a `Matrix` class that can be initialized with a square grid of floating point numbers. It must have methods for transposition, clockwise rotation, anticlockwise rotation, horizontal reflection, and vertical reflection. All the methods take zero parameters and should modify the matrix _in place_, using only `O(1)` extra space, and return nothing.

# Example 1: Transposition
# grid = [[1, 2],
#         [3, 4]]
# After transpose():
#        [[1, 3],
#         [2, 4]]

# Example 2: Clockwise Rotation
# grid = [[1, 2],
#         [3, 4]]
# After rotate_clockwise():
#        [[3, 1],
#         [4, 2]]

# Example 3: Horizontal Reflection
# grid = [[1, 2],
#         [3, 4]]
# After reflect_horizontally():
#        [[2, 1],
#         [4, 3]]

# Constraints:

# - 1 ≤ n ≤ 1000 where n is the size of the square matrix
# - -10^4 ≤ grid[i][j] ≤ 10^4