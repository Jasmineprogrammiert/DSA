# Find the positons of 1, then get the smallest row index (distance between river and cloest footprint)
# Check cells in the first column to find 1
# For remaining columns C-1, only check up to 3 cells
# Time Complexity: O(R + (C-1)*3) = O(R+C)

# R: length of row
# C: length of column
# T: O(R+C)
# O: O(1)

def snow_prints(field):
    R, C = len(field), len(field[0])
    r, c = 0, 0
    direction = [-1, 0, 1]
    
    def is_footprint(r, c):
        return 0 <= r < R and 0 <= c < C and field[r][c] == 1
    
    while field[r][0] != 1:
        r += 1
    min_r = r
    
    while c < C - 1: # so that 'new_c = c + 1' won't be out of bound
        for dir in direction:
            new_r = r + dir
            new_c = c + 1
            if is_footprint(new_r, new_c):
                r, c = new_r, new_c
                min_r = min(min_r, r)
                break
            
    return min_r

# def snow_prints(field):
#     R, C = len(field), len(field[0])
    
#     for r in range(R):
#         if field[r][0] == 1:
#             curr_r = r
#             break
    
#     min_r = curr_r
    
#     for c in range(1, C):
#         for dir in [-1, 0, 1]:
#             r = curr_r + dir
#             if 0 <= r < R and field[r][c] == 1:
#                 curr_r = r
#                 break
#         min_r = min(min_r, curr_r)
    
#     return min_r



# # Snowprints

# We are tracking _Elsa_, an arctic fox, through a rectangular snowy field represented by a binary grid, `field`, where `1` denotes snowprints and `0` denotes no snowprints. We know that the fox crossed the field from left to right, so each column has exactly one `1`. Between two consecutive columns, the row of the `1` may remain the same, go up by one, or go down by one. Above the field (above the first row), there is an icy river. Return how close the fox got to the river, in terms of the number of rows between it and the river.

# Example 1:
# field = [[0, 0, 0, 0, 0, 0],
#          [0, 0, 1, 0, 0, 0],
#          [1, 1, 0, 1, 0, 0],
#          [0, 0, 0, 0, 1, 1]]
# Output: 1
# Explanation: The fox was closest to the river at column 2 (0-based), where it was 1 row away.

# Example 2:
# field = [[0, 0, 0, 1, 0, 0],
#          [0, 0, 1, 0, 1, 0],
#          [1, 1, 0, 0, 0, 1],
#          [0, 0, 0, 0, 0, 0]]
# Output: 0
# Explanation: The fox touched row 0, which is right next to the river.

# Example 3:
# field = [[1, 1, 1]]
# Output: 0
# Explanation: The fox stayed in row 0 the whole time.

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/snowprints-1.png
# Above is a picture representation of Example 1.

# Constraints:

# - `1 ≤ R, C ≤ 1000`, where `R` is the number of rows and `C` is the number of columns
# - `field[i][j]` is either `0` or `1`
# - Each column has exactly one `1`
# - The fox's path is valid (moves at most one row up/down between columns)