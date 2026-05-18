# Problem 36.9 - First Time All Connected
# Given V >= 2 computers and a list of cables [x, y] added in order,
# return the index of the cable after which all computers are connected,
# or -1 if never.
#
# Example 1: V = 4, cables = [[0,2],[1,3],[0,1],[1,2]] -> 2
# Example 2: V = 3, cables = [[0,1]] -> -1
# Example 3: V = 4, cables = [[0,1],[1,2],[2,0],[2,3],[3,0]] -> 3
#
# Constraints:
# - 2 <= V <= 10^4
# - 0 <= E <= 10^5
# - All cables are unique