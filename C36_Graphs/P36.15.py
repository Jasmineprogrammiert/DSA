# 1. No obstacles -> BFS layer distance == taxicab distance, so multi-source BFS works
# 2. 3 passes (R->G, G->B, B->R): seed all `source` cells at 0, flood, write dist at `target` cells
# 3. Fixing source/target: dist[x] = distance to NEAREST source, so 
# output[target] = dist to nearest source -> 
# output[R] = nearest G -> 
# visit('G', 'R')
#    i.e. seed the color you want to be NEAR, answer at the color that's ASKING
#
# n: elements in screen (rows * cols)
# T: O(n) - 3 passes; seed scan + each cell enqueued once, 4 neighbor checks per pop
# S: O(n) - output + per-pass dist grid and queue

from collections import deque


def rgb_distance(screen):
    R, C = len(screen), len(screen[0])
    output = [[0] * C for _ in range(R)]
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    rules = {'R': 'G', 'G': 'B', 'B': 'R'}

    def visit(source, target):
        dist = [[-1] * C for _ in range(R)]
        queue = deque()

        for r in range(R):
            for c in range(C):
                if screen[r][c] == source:
                    dist[r][c] = 0
                    queue.append((r, c))

        while queue:
            r, c = queue.popleft()
            if screen[r][c] == target:
                output[r][c] = dist[r][c]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))
    
    for target, source in rules.items():
        visit(source, target)

    return output


# # RGB Distances

# The _taxicab distance_ between two cells `(r1, c1)` and `(r2, c2)` in a grid is defined as `abs(r1 - r2) + abs(c1 - c2)`.

# You are given a grid of characters, `screen`, representing a screen with `rows x cols` pixels, where each element is one of `'R'`, `'G'`, or `'B'`.

# Return a grid, `output`, with the same dimensions, where:

# - If `screen[i][j] = 'R'`, `output[i][j]` is the taxicab distance from `screen[i][j]` to the closest `'G'`
# - If `screen[i][j] = 'G'`, `output[i][j]` is the taxicab distance from `screen[i][j]` to the closest `'B'`
# - If `screen[i][j] = 'B'`, `output[i][j]` is the taxicab distance from `screen[i][j]` to the closest `'R'`

# It is guaranteed that the screen contains at least one `'R'`, one `'G'`, and one `'B'`.

# Example 1:
# screen = [
#   "RRRGRB",
#   "BGRGRR",
#   "RRRGRR",
#   "RGRRRR",
#   "GBGRGG"
# ]

# Output: [
#   [2, 1, 1, 2, 1, 1],
#   [1, 1, 1, 3, 1, 2],
#   [2, 1, 1, 4, 1, 2],
#   [1, 1, 1, 1, 1, 1],
#   [1, 2, 1, 1, 3, 4]
# ]

# Example 2:
# screen = [
#   "RGB"
# ]

# Output: [
#   [1, 1, 2]
# ]

# Constraints:

# - `1 <= rows, cols <= 1000`
# - `screen[i][j]` is one of `'R'`, `'G'`, or `'B'`
# - `screen` contains at least one of each color
# - All the rows have the same length