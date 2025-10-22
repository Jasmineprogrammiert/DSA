# Problem: 
    # given the rule and location of either King, Knight and Queen, 
    # return a list of all the unoccupied cells that can be reached in one move

# Rules:
    # King: any adjacent cells (including diagonals) by one cell
    # Knight: jump one cell by one dimension, then two in the other
    # Queen: any number of cells in any directions, but cannot go through occupied cells

# Given:
    # board: n*n binary grid, with 1 as occupied cell
    # piece: either king, knight or queen
    # piece's location: (r, c)

# Thought Process:
    # King/Nnight: list all possible moves, 
    # check if each cell is within bounds and not occupied
    # only checks the first cell in each direction
    
    # Queen: for each direction, keeps moving till an obstable or edge of bound is hit
    # add each valid cell along the way
    
    # cell's validaty check:
        # 0 <= r < len(board)
        # 0 <= c < len(board[0])
        # board[r][c] != 1
    # moves = []: store valid moves of any piece

# Directions:
    # king_and_queen_directions = [
    #     [-1, 0], [1, 0], [0, -1], [0, 1], # vertical and hotizontal
    #     [-1, -1], [-1, 1], [1, 1], [1, -1] # diagonal
    # ]

    # knight_directions = [
    #     [-1, -2], [-2, -1], [-2, 1], [-1, 2], # upper four
    #     [1, -2], [2, -1], [2, 1], [1, 2] # lower four
    # ]

# n: board size
# T: O(1) for king and knight, O(n) for queen
# S: O(1) for king and knight, O(n) for queen

def chess_moves(board, piece, r, c):    
    def is_valid(r, c):
        return 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] != 1
    
    moves = []
    king_and_queen_directions = [
        [-1, 0], [1, 0], [0, -1], [0, 1],
        [-1, -1], [-1, 1], [1, 1], [1, -1]
    ]
    knight_directions = [
        [-1, -2], [-2, -1], [-2, 1], [-1, 2],
        [1, -2], [2, -1], [2, 1], [1, 2]
    ]
    
    if piece == 'knight':
        directions = knight_directions
    else:
        directions = king_and_queen_directions
    
    for dir_r, dir_c in directions:
        new_r, new_c = r + dir_r, c + dir_c
        
        if piece == 'queen':
            while is_valid(board, new_r, new_c):
                moves.append([new_r, new_c])
                new_r += dir_r
                new_c += dir_c
        elif is_valid(board, new_r, new_c):
            moves.append([new_r, new_c])
        
    return moves



# # Chess Moves

# For context, this is how the King, Knight, and Queen move on a chessboard:

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/chess-moves-1.png

# The king can go to any adjacent cell, including diagonals. The knight 'jumps' one cell in one dimension and two in the other, even if there are pieces in between. The queen can move _any number of cells_ in any direction, including diagonals, but cannot go through occupied cells.

# We are given three inputs:

# - `board`, an `nxn` binary grid, where a `0` denotes an empty cell, `1` denotes an occupied cell (for this problem, it doesn't matter what piece is in it)
# - `piece`, which is one of `"king"`, `"knight"`, or `"queen"`
# - `r` and `c`, with `0 ≤ r < n` and `0 ≤ c < n`, which denote an unoccupied position in the board

# Return a list of all the **unoccupied** cells in `board` that can be reached by the given `piece` in one move starting from `[r, c]`. The order of the output cells does not matter.

# Example 1:
# board = [[0, 0, 0, 1, 0, 0],
#          [0, 1, 1, 1, 0, 0],
#          [0, 1, 0, 1, 1, 0],
#          [1, 1, 1, 1, 0, 0],
#          [0, 0, 0, 0, 0, 0],
#          [0, 1, 0, 0, 0, 0]]
# piece = "king"
# r = 3
# c = 5
# Output: [[2, 5], [3, 4], [4, 4], [4, 5]]

# Example 2:
# board = [[0, 0, 0, 1, 0, 0],
#          [0, 1, 1, 1, 0, 0],
#          [0, 1, 0, 1, 1, 0],
#          [1, 1, 1, 1, 0, 0],
#          [0, 0, 0, 0, 0, 0],
#          [0, 1, 0, 0, 0, 0]]
# piece = "knight"
# r = 4
# c = 3
# Output: [[2, 2], [3, 5], [5, 5]]

# Example 3:
# board = [[0, 0, 0, 1, 0, 0],
#          [0, 1, 1, 1, 0, 0],
#          [0, 1, 0, 1, 1, 0],
#          [1, 1, 1, 1, 0, 0],
#          [0, 0, 0, 0, 0, 0],
#          [0, 1, 0, 0, 0, 0]]
# piece = "queen"
# r = 4
# c = 4
# Output: [[3, 4], [3, 5], [4, 0], [4, 1], [4, 2], [4, 3], [4, 5], [5, 3], [5, 4], [5, 5]]

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/chess-moves-2.png

# Constraints:

# - `1 ≤ n ≤ 100`
# - `board[i][j]` is either `0` or `1`
# - `0 ≤ r, c < n`
# - `piece` is one of `"king"`, `"knight"`, or `"queen"`