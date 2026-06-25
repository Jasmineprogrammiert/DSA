# Problem 43.6 - Count Subarrays With Sum K
# Given an array of integers, arr, and an integer k, return the number of
# subarrays in arr with sum k.
#
# Example 1:
# arr = [1, 2, 3, 2, 1], k = 3
# Output: 3
# The subarrays with sum 3 are [1, 2], [3], and [2, 1].
#
# Example 2:
# arr = [-1, -2, -3, 2, 1], k = -3
# Output: 4
# The subarrays with sum -3 are [-1, -2], [-3], [-2, -3, 2],
# and [-1, -2, -3, 2, 1].
#
# Constraints:
# - len(arr) <= 10^5
# - Each element in arr is an integer between -10^4 and 10^4