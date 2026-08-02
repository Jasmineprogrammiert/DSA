# (r,c) -> (c,n-1-r), order 4 -> 4-cycles
# A=(r,c) B=(c,n-1-r) C=(n-1-r,n-1-c) D=(n-1-c,r)   <- SLOTS, not values
# values travel clockwise, so assignments run the other way:
#     temp=A; A=D; D=C; C=B; B=temp
# r in range(n//2), c in range((n+1)//2)   -> one per cycle

# n: matrix side
# T: O(n^2) — n^2/4 cycles, O(1) each
# S: O(1) — one temp per cycle


# # Matrix Rotation

# Given a square `n x n` matrix, `mat`, rotate it 90 degrees clockwise in place, using `O(1)` extra space.

# Example: mat =  [[25, 15],
#                  [10, 30]]
# Output:    mat = [[10, 25],
#                  [30, 15]]
# We should not create a new matrix.

# Example: mat = [[1, 2, 3],
#                 [4, 5, 6],
#                 [7, 8, 9]]
# Output:  mat = [[7, 4, 1],
#                 [8, 5, 2],
#                 [9, 6, 3]]

# Constraints:

# - `1 <= n <= 1000` where `n` is the size of the square matrix
# - `-10^9 <= mat[i][j] <= 10^9` (matrix elements are integers)