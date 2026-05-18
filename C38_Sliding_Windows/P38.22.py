# Problem 38.22 - Count Subarrays With Drops
# Given array arr and k, count subarrays with at most / exactly / at least
# k drops. A drop is consecutive pair where first > second.
# Return [at_most, exactly, at_least].
#
# Example 1: arr = [1,2,3], k = 1 -> [6,0,0]
# Example 2: arr = [3,2,1], k = 1 -> [5,2,3]
# Example 3: arr = [5,4,3,2,1], k = 2 -> [12,3,6]
#
# Constraints:
# - 0 <= arr.length <= 10^5
# - -10^9 <= arr[i] <= 10^9
# - 0 <= k <= 10^5