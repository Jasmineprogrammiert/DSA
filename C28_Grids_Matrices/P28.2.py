# 1. Create an empty board of the same size as the original board
# 2. Find out queen's location(s)
# 3. For each queen:
    # Mark its cell as 1 in the new board
    # Mark all cells it can reach by one move as 1

# n: board size
# T: O(n^2) - O(n^2) cells, each can be reached max 8 times
# S: O(n^2) - a new grid with the same size is created

def queen_reach(board):
    n = len(board)
    res = [[0] * n for _ in range(n)]
    
    directions = [
        [0, -1], [0, 1], [-1, 0], [1, 0],
        [-1, -1], [1, 1], [-1, 1], [1, -1]
    ]
    
    def is_valid(r, c):
        return 0 <= r < n and 0 <= c < n and board[r][c] != 1
    
    def label_invalid_cells(r, c):
        for dir_r, dir_c in directions:
            new_r = r + dir_r
            new_c = c + dir_c
            
            while is_valid(new_r, new_r):
                res[new_r][new_r] = 1
                new_r += dir_r
                new_c += dir_c
        
    for r in range(n):
        for c in range(n):
            if board[r][c] == 1:
                res[r][c] == 1
                label_invalid_cells(r, c)
    
    return res



# # Queen's Reach

# Imagine that an `n x n` chessboard has a number of queens in it. Remember that in chess, a queen can move any number of cells horizontally, vertically, or diagonally.

# We are given an `nxn` binary grid, `board`, with `n > 0`, where `0` indicates that the cell is unoccupied, and a `1` indicates a queen (the color of the queen doesn't matter). Return a binary board with the same dimensions. In the returned board, `0` denotes that a cell is 'safe', and a `1` denotes that a cell is not safe. A cell is _safe_ if there isn't a queen in it and no queen on the board can reach it in a single move.

# Example 1:
# board = [[0, 0, 0, 1],
#          [0, 0, 0, 0],
#          [0, 0, 0, 0],
#          [1, 0, 0, 0]]
# Output: [[1, 1, 1, 1],
#          [1, 0, 1, 1],
#          [1, 1, 0, 1],
#          [1, 1, 1, 1]]

# Example 2:
# board = [[1]]
# Output: [[1]]
# Explanation: The only cell has a queen, so it's not safe.

# Example 3:
# board = [[0]]
# Output: [[0]]
# Explanation: With no queens, all cells are safe.

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/queens-reach-1.png

# Constraints:

# - `1 ≤ n ≤ 100`
# - `board[i][j]` is either `0` or `1`