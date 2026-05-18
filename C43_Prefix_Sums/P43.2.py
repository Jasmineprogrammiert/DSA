# Problem 43.2 - YouTube Video Reception
# A day is positive if it has more likes than dislikes. Given:
# - Two arrays likes and dislikes of length n.
# - An array periods of length p, where each element is a pair [l, r]
#   with 0 <= l <= r < n.
# Return an array results of length p, where results[i] is the number of
# positive days during period[i].
#
# Example:
# likes    = [6, 3, 4, 8, 7, 2, 6, 5, 0, 1]
# dislikes = [6, 0, 8, 0, 0, 0, 1, 8, 0, 2]
# periods  = [[0, 1], [0, 5], [5, 8], [3, 3]]
# Output: [1, 4, 2, 1]
#
# Constraints:
# - len(likes) == len(dislikes) <= 10^5
# - Each element in likes and dislikes is a non-negative integer < 10^4
# - len(periods) <= 10^5
# - periods[i].length == 2
# - 0 <= periods[i][0] <= periods[i][1] < n
