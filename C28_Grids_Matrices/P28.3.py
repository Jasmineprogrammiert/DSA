# n = 3
# Output: [[4, 5, 6],
#          [3, 0, 7],
#          [2, 1, 8]]

# 0 0 6     RES
# 0 0 7
# 0 0 8

# val = 6
# dir_idx = 0

# r, c = 0, 2
# dr, dc = -1, 0
# nxt_r, nxt_c = -1, 2

# n: number of rows and columns
# T: O(n^2) - initialize n * n cells, then n * n - 1 iterations with O(1) operations each
# S: O(n^2) - res stores n * n cells; auxiliary variables take O(1)

def spiral_order(n):
    res = [[0] * n for _ in range(n)]
    val = n * n - 1
    r = c = n - 1
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    dir_idx = 0
    res[r][c] = val

    while val > 0:
        dr, dc = directions[dir_idx]
        nxt_r, nxt_c = r + dr, c + dc

        if not (
            0 <= nxt_r < n
            and 0 <= nxt_c < n
            and res[nxt_r][nxt_c] == 0
        ):
            dir_idx = (dir_idx + 1) % 4
            dr, dc = directions[dir_idx]
            nxt_r, nxt_c = r + dr, c + dc

        val -= 1
        res[nxt_r][nxt_c] = val
        r, c = nxt_r, nxt_c

    return res


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