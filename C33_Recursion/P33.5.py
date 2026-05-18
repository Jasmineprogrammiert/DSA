# Problem 33.5 - Laminal Arrays
# Given an array arr whose length is a power of 2.
# The set of laminal arrays is defined as:
# - arr itself is laminal.
# - Each half of a laminal array with even length is laminal.
# Find the laminal array with maximum sum and return its sum.
#
# Example 1: arr = [3, -9, 2, 4, -1, 5, 5, -4] -> 6
#   Laminal arrays: [3,-9,2,4,-1,5,5,-4], [3,-9,2,4], [-1,5,5,-4],
#   [3,-9], [2,4], [-1,5], [5,-4], [3], [-9], [2], [4], [-1], [5], [5], [-4]
#   Maximum sum is [2, 4] = 6
# Example 2: arr = [1] -> 1
# Example 3: arr = [-1, -2] -> -1
# Example 4: arr = [1, 2, 3, 4] -> 10
# Example 5: arr = [-2, -1, -4, -3] -> -1
#
# Constraints:
# - len(arr) is a power of 2
# - 1 <= len(arr) <= 10^5
# - -10^9 <= arr[i] <= 10^9