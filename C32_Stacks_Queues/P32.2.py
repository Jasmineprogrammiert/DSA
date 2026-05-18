# Problem 32.2 - Compress Array By K
# Given an array of integers and an integer k >= 2, a k-compress operation finds
# the first block of k consecutive equal numbers and combines them into their sum.
# Repeatedly apply k-compress until fully k-compressed.
#
# Example 1: arr = [1, 9, 9, 3, 3, 3, 4], k = 3 -> [1, 27, 4]
# Example 2: arr = [8, 4, 2, 2], k = 2 -> [16]
# Example 3: arr = [4, 4, 4, 4], k = 5 -> [4, 4, 4, 4]
#
# Constraints:
# - len(arr) <= 10^5
# - Each element is a non-negative integer < 10^3
# - 2 <= k <= 10^5