# RETURN: `true` if the board does not have any conflicts and `false` otherwise
# A conflict is a duplicate number (other than 0) along a row, a column, or a 3x3 subgrid (shown with the thicker outline)

# T: O(1) - fixed 9x9 board; each cell is checked in its row, column and subgrid
# S: O(1) - seen and cells hold at most 9 values each; the board size is fixed

def valid_sudoku(board):
    def no_duplicates(values):
        seen = set()
        for val in values:
            if val == 0:
                continue
            elif val in seen:
                return False
            else:
                seen.add(val)
        return True

    for row in board:
        if not no_duplicates(row):
            return False

    for col in zip(*board):
        if not no_duplicates(col):
            return False

    for start_r in range(0, 9, 3):
        for start_c in range(0, 9, 3):
            cells = []
            for r in range(3):
                for c in range(3):
                    cells.append(board[start_r + r][start_c + c])
            if not no_duplicates(cells):
                return False
    return True


# # Valid Sudoku

# Given a 9x9 grid `board` representing a Sudoku, return `true` if the board does not have any conflicts and `false` otherwise. The board contains only numbers between 0 and 9 in each cell, with 0's denoting empty cells.

# A conflict is a duplicate number (other than 0) along a row, a column, or a 3x3 subgrid (shown with the thicker outline). For the purposes of this problem, it doesn't matter if the Sudoku has a valid solution or not -- only whether it has a conflict in the already-filled cells.

# For those who don't know the rules of Sudoku: the grid starts off with some cells pre-filled with numbers. The player is asked to fill in the empty cells with the numbers 1 through 9, such that there are no duplicates in the same row, column, or subgrid (the 3x3 sections shown with the thicker outline).

# Example 1:
# board = +-------+-------+-------+
#         | 5 . . | . . . | . . 6 |
#         | . . 9 | . 5 . | 3 . . |
#         | . 3 . | . . 2 | . . . |
#         +-------+-------+-------+
#         | 8 . . | 7 . . | . . 9 |
#         | . . 2 | . . . | 8 . . |
#         | 4 . . | . . 6 | . . 3 |
#         +-------+-------+-------+
#         | . . . | 3 . . | . 4 . |
#         | . . 3 | . 8 . | 2 . . |
#         | 9 . . | . . . | . . 7 |
#         +-------+-------+-------+
# Output: true

# Example 2:
# board = +-------+-------+-------+
#         | 5 . . | . . . | . . 6 |
#         | . . 9 | . 5 . | 3 . . |
#         | . 3 . | . . 2 | . . . |
#         +-------+-------+-------+
#         | 8 . . | 7 . . | . . 9 |
#         | . . 2 | . . . | 8 . . |
#         | 4 . . | . . 6 | . . 3 |
#         +-------+-------+-------+
#         | . . . | 3 . . | . 4 . |
#         | . . 3 | . 8 . | 7 . . |
#         | 9 . . | . . . | . . 7 |
#         +-------+-------+-------+
# Output: false
# Explanation: The bottom-right 3x3 subgrid has a duplicate, 7.

# Example 3:
# board = +-------+-------+-------+
#         | . . . | . . . | . . . |
#         | . . . | . . . | . . . |
#         | . . . | . . . | . . . |
#         +-------+-------+-------+
#         | . . . | . . . | . . . |
#         | . . . | . . . | . . . |
#         | . . . | . . . | . . . |
#         +-------+-------+-------+
#         | . . . | . . . | . . . |
#         | . . . | . . . | . . . |
#         | . . . | . . . | . . . |
#         +-------+-------+-------+
# Output: true
# Explanation: An empty board has no conflicts.

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/valid-sudoku-1.png

# Constraints:

# - board.length == 9
# - board[i].length == 9
# - board[i][j] is a digit between 0 and 9.