# Jump if the closest points on two pieces are at most d apart.
# [x_min, y_min, x_max, y_max]: x uses indices 0, 2; y uses 1, 3.
# For each axis, the gap is 0 if the ranges overlap; compare dx*dx + dy*dy to d*d.

# furniture = [                 d = 5
#   [1, 1, 9, 5],
#   [12, 9, 20, 13],
#   [16, 2, 22, 7],
#   [24, 9, 26, 11],
#   [29, 1, 31, 5]
# ]
# --> True

# piece popped   newly reachable   queue after   seen after
# start          -                 [0]           {0}
# 0              1                 [1]           {0, 1}
# 1              2, 3              [2, 3]        {0, 1, 2, 3}
# 2              none              [3]           {0, 1, 2, 3}
# 3              4                 [4]           {0, 1, 2, 3, 4}
# 4              destination       -             return True

# n: number of furniture pieces
# T: O(n^2) - each piece is explored once; each exploration checks up to n pieces
# S: O(n) - the visited set and queue each hold at most n piece indices

from collections import deque

def is_lava(furniture, d):
    def can_jump(a, b):
        if a[2] < b[0]:
            dx = b[0] - a[2]
        elif b[2] < a[0]:
            dx = a[0] - b[2]
        else:
            dx = 0

        if a[1] > b[3]:
            dy = a[1] - b[3]
        elif b[1] > a[3]:
            dy = b[1] - a[3]
        else:
            dy = 0

        return dx * dx + dy * dy <= d * d

    queue = deque([0])
    visited = {0}
    n = len(furniture)
    while queue:
        piece = queue.popleft()
        if piece == n - 1:
            return True
        for nbr in range(n):
            if nbr not in visited and can_jump(furniture[piece], furniture[nbr]):
                visited.add(nbr)
                queue.append(nbr)
    return False


# # The Floor Is Lava

# We are given an array, `furniture`, where each element consists of four integer coordinates, `[x_min, y_min, x_max, y_max]`, indicating the boundary of a rectangular piece of furniture. The furniture pieces are non-overlapping (they can share an edge or a corner).

# We are playing the game 'the floor is lava,' where we have to reach from the first piece of furniture (the one at index `0` in `furniture`) to the last one without touching the floor, only jumping on furniture. If we can jump at most a distance of `d`, where `d` is an integer, can we win?

# Recall that:

# `distance((x1, y1), (x2, y2)) = sqrt((x1 - x2)^2 + (y1 - y2)^2)`.

# For example, if this is the furniture and `d` is `5`, we can jump from the furniture labeled `0` to the one labeled `4` with the indicated jumps:

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/the-floor-is-lava-1.png

# However, if `d` is `4` for the same furniture, we can't do it.

# Example 1:
# furniture = [
#   [1, 1, 9, 5],
#   [12, 9, 20, 13],
#   [16, 2, 22, 7],
#   [24, 9, 26, 11],
#   [29, 1, 31, 5]
# ]
# d = 5

# Output: True
# See the image above

# Example 2:
# furniture = [
#   [1, 1, 9, 5],
#   [12, 9, 20, 13],
#   [16, 2, 22, 7],
#   [24, 9, 26, 11],
#   [29, 1, 31, 5]
# ]
# d = 4
# Output: False
# See the image above

# Constraints:

# - `1 <= furniture.length <= 1000`
# - `furniture[i]` is a list of `4` integers
# - `0 <= furniture[i][0] < furniture[i][2] < 10^9`
# - `0 <= furniture[i][1] < furniture[i][3] < 10^9`
# - The furniture pieces are non-overlapping
# - `0 < d <= 10^9`
# - All coordinates and distances are floating-point numbers