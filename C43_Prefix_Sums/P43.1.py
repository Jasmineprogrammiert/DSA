# Problem 43.1 - Channel Views
# Given:
# - An array views of length n > 0, where views[i] is the number of views
#   on day i.
# - An array periods of length p > 0, where each element is a pair [l, r]
#   with 0 <= l <= r < n, representing a time period from day l to day r
#   inclusive.
# Return an array results of length p, where results[i] is the number of
# views during period i.
#
# Example:
# views = [3, 5, 4, 8, 7, 2, 5, 3, 2, 3]
# periods = [[0, 1], [0, 5], [5, 8], [3, 3]]
# Output: [8, 29, 12, 8]
#
# Constraints:
# - len(views) <= 10^5
# - 0 <= views[i] < 10^4
# - len(periods) <= 10^5
# - periods[i].length == 2
# - 0 <= periods[i][0] <= periods[i][1] < n