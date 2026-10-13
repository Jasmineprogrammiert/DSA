# 0 = walkable, 1 = obstacle, 2 = clue
# Start (0,0); move up/down/left/right without revisiting cells
# Return the shortest path collecting all clues, or [] if impossible
# At least one clue; any shortest path is valid

# 0 1 0
# 0 2 0
# 0 0 2
# Output: [[0,0], [1,0], [1,1], [1,2], [2,2]]

# path:  (0,0) -> (1,0) -> (1,1) -> (1,2) -> (2,2)
# clues:   0        0        1        1        2     save

# N: number of cells, R * C
# T: O(N * 3^N) - loose bound: up to 3 onward moves per step, O(N) per best-path copy
# S: O(N) - call stack, visited, path and best

def escape_with_clues(room):
    DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    R, C = len(room), len(room[0])
    visited = {(0, 0)}
    path = [[0, 0]]
    total_clues = 0

    for row in room:
        for item in row:
            if item == 2:
                total_clues += 1

    best = None

    def visit(r, c, collected):
        nonlocal best
        if collected == total_clues:
            if best is None or len(path) < len(best):
                best = path.copy()
            return

        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc

            if (0 <= nr < R and 0 <= nc < C
                and room[nr][nc] != 1
                and (nr, nc) not in visited):
                visited.add((nr, nc))
                path.append([nr, nc])
                visit(nr, nc, collected + (1 if room[nr][nc] == 2 else 0))
                path.pop()
                visited.remove((nr, nc))

    visit(0, 0, 0)
    return best if best is not None else []


# # Escape With All Clues

# We are building an escape room puzzle where a player has to collect all the clues in a room to unlock the way out. The room is represented by a non-empty grid, `room`, consisting of walkable spaces (`0`), obstacles (`1`), and clues (`2`). The player starts on the top-left cell of the grid, which is guaranteed to be an open space, and can move to adjacent cells (diagonals not allowed). If it is possible to collect all the clues **without repeating any cell**, return an array with the list of cells in the shortest path to collect them, starting with `[0, 0]`. Otherwise, return an empty array. If there are multiple shortest paths, return any of them. It is guaranteed that there is at least one clue.

# Example 1: room = [[0, 1, 0],
#                    [0, 2, 0],
#                    [0, 0, 2]]
# Output: [[0,0], [1,0], [1,1], [1,2], [2,2]]. The other valid output is [[0,0], [1,0], [1,1], [2,1], [2,2]].

# Example 2: room = [[0, 0, 0],
#                    [2, 1, 2]]
# Output: []. It is not possible to get both clues without revisiting a cell.

# Example 3: room = [[0, 0, 1, 2],
#                    [0, 1, 0, 0]]
# Output: []. It is not possible to reach the clue.

# Constraints:

# - `room` is a 2D grid of `0`s, `1`s, and `2`s.
# - `room` has at least one `2`.
# - `room[0][0]` is `0`.
# - `room` has at least `1` to `6` rows and `1` to `6` columns.