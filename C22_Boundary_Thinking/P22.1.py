# # Tunnel Depth

# We are given an `n x n` binary matrix, `tunnel_network`, representing a tunnel network that archeologists have excavated. The ground level is above the first row. The first row is at depth `0`, and each subsequent row is deeper underground.

# - 1's represent excavated tunnel pathways in the network.
# - 0's represent earth that has not been excavated yet.

# The tunnel starts at the top-left and top-right corners (the cells `(0, 0)` and `(0, n - 1)` are always 1's) and consists of a single connected network. That is, this is not a valid input because there is a `1` that is not reachable:

# tunnel_network = [
#   [1,0,0,1],
#   [1,1,1,1],
#   [0,0,0,0],
#   [1,0,0,0],
# ]

# Write a function that returns the maximum tunnel depth.

# Example 1:
# Input: tunnel_network = [
#   [1,0,0,0,1],  # depth 0
#   [1,1,1,0,1],  # depth 1
#   [1,0,1,0,1],  # depth 2
#   [1,1,1,1,1],  # depth 3
#   [0,0,0,0,0]   # depth 4
# ]
# Output: 3
# Explanation: The deepest row containing a 1 is row 3 (0-indexed).

# Example 2:
# Input: tunnel_network = [
#   [1,1,0,0,0,1],
#   [0,1,0,0,0,1],
#   [1,1,0,0,0,1],
#   [1,0,0,0,0,1],
#   [1,1,0,0,0,1],
#   [0,1,1,1,1,1]
# ]
# Output: 5
# Explanation: The deepest row containing a 1 is row 5.

# Example 3:
# Input: tunnel_network = [[1]]
# Output: 0
# Explanation: The only row containing a 1 is row 0.

# Constraints:

# - `1 <= n <= 10^4`
# - `tunnel_network[i][j]` is either `0` or `1`
# - `tunnel_network[0][0]` and `tunnel_network[0][n-1]` are both `1`
# - All `1`s in the grid form a single connected component