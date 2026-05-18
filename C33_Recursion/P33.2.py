# Problem 33.2 - Nested Array Sum
# A nested array is an array where each element is either an integer or a nested
# array (recursive definition). The sum of a nested array is defined recursively
# as the sum of all its elements. Given a nested array arr, return its sum.
#
# Example 1: arr = [1, [2, 3], [4, [5]], 6] -> 21
# Example 2: arr = [[[[1]], 2]] -> 3
# Example 3: arr = [] -> 0
# Example 4: arr = [[], [1, 2], [], [3]] -> 6
# Example 5: arr = [-1, [-2, 3], [4, [-5]], 6] -> 5
#
# Constraints:
# - Nesting depth <= 500
# - Each integer is between -10^9 and 10^9
# - Total number of integers <= 10^5