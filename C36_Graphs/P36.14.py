# Multi-source BFS skeleton:
#   seed the queue with ALL sources at distance 0, then expand in layers.
#   First time a cell is reached = its shortest distance to any source.
#
# n: R * C  (total cells)
# T: O(n) — scan all cells once to seed; each cell enqueued at most once
#           (stamped != -1 the instant it's enqueued), 4 neighbor checks
#           per dequeue -> O(4n) = O(n)
# S: O(n) — dist grid + queue (worst case holds O(n) cells)

from collections import deque


def multi_exit_maze(maze):
    R, C = len(maze), len(maze[0])
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    dist = [[-1] * C for _ in range(R)]
    queue = deque()

    for r in range(R):
        for c in range(C):
            if maze[r][c] == "O":
                dist[r][c] = 0
                queue.append((r, c))

    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (0 <= nr < R and 0 <= nc < C and
                    maze[nr][nc] != "X" and dist[nr][nc] == -1):
                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))

    return dist


# # Multi-Exit Maze

# A few friends are trapped on a maze represented by a grid of letters:

# - `'X'` represents a wall.
# - `'O'` represents an exit. There may be multiple exits.
# - `'.'` represents a walkable space.

# Given the grid, `maze`, return a grid with the same dimensions.
# Each cell `(r, c)` should contain the minimum number of steps needed to go from position `(r, c)` in the maze to the closest exit.
# If `(r, c)` is a wall in the maze, return `-1` at that position.
# It is guaranteed that every walkable cell can reach an exit.

# Example 1:
# maze = [
#   "...X.O",
#   "OX.X..",
#   "...X..",
#   ".X....",
#   "XOX.XX"
# ]
# Output: [
#   [ 1,  2,  3, -1,  1,  0],
#   [ 0, -1,  4, -1,  2,  1],
#   [ 1,  2,  3, -1,  3,  2],
#   [ 2, -1,  4,  5,  4,  3],
#   [-1,  0, -1,  6, -1, -1]
# ]

# Example 2:
# maze = [
#   "...",
#   ".O.",
#   "..."
# ]
# Output: [
#   [2, 1, 2],
#   [1, 0, 1],
#   [2, 1, 2]
# ]

# Constraints:

# - `1 <= maze.length <= 1000`
# - `1 <= maze[i].length <= 1000`
# - `maze[i][j]` is either `'.'`, `'X'`, or `'O'`
# - All the rows have the same length