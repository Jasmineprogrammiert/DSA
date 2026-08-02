# node = player, edge = same row/col with nobody between
#     sort each row by col, join CONSECUTIVE (mirror for cols) -> m = O(n)
# a component never empties; BFS + delete furthest-first takes it to 1
# -> answer = number of connected components
#
# for node in graph:
#     if node not in visited: count += 1; BFS(node, visited)

# n: players
# T: O(n log n) — sorting each row/col group to find consecutive players;
#    the traversal itself is O(n + m) with m = O(n)
# S: O(n) — adjacency plus visited


# # Multiplayer Video Game

# A group of `n` friends is playing a videogame with the following rules:

# 1. Each player starts at some unique `(x, y)` integer coordinates in the videogame map.
# 2. Players cannot move.
# 3. A player can shoot and eliminate another player if they have the same `x` coordinate or `y` coordinate and no other player is between them (eliminated or not). Players cannot shoot in directions not aligned with the `x`-axis or the `y`-axis.
# 4. Players can shoot more than once.
# 5. Two players cannot shoot simultaneously.
# 6. Once a player is eliminated, they cannot shoot anymore.

# The game starts, and players shoot each other until no remaining player can shoot anyone else. Find the order of shots that minimizes the final number of players standing, and return that number.

# Example 1: players = [(1, 1), (1, 5), (5, 1), (5, 5)]

# .......
# .A...B.
# .......
# .......
# .......
# .D...C.
# .......

# Output: 1. If (1) A shoots B, (2) D shoots C, and (3) D shoots A, the only player remaining will be D, so the answer is 1. There are other ways we could get down to 1 player.

# Example 2: players = [(2, 0), (0, 2), (0, 6), (2, 4), (4, 6), (6, 4)]

# ..B...C
# .......
# A...D..
# .......
# ......E
# .......
# ....F..

# Output: 2. C can shoot B and E, and D can shoot A and F, so we can get down to 2 players. No matter who shoots who, there is no way to have only one player left, so the answer is 2.

# Example 3: players = [(0, 0), (0, 1), (0, 6), (1, 0), (1, 1), (2, 2), (2, 4), (4, 2), (4, 4), (4, 6), (6, 3), (6, 4), (6, 5)]

# AB....C
# DE.....
# ..F.G..
# .......
# ..H.I.J
# .......
# ...KLM.

# Output: 1.

# Constraints:

# - `0 <= n <= 10^5` where `n` is the number of players
# - `-10^9 <= x, y <= 10^9` for each player position `(x, y)`
# - All player positions are unique
# - Each player starts at integer coordinates

# Below are all three examples visualized in an illustration.

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/multiplayer-video-game-1.png