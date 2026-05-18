# Problem 32.1 - Compress Array
# Given an array of integers, a compress operation finds the first pair of
# consecutive equal numbers and combines them into their sum. If there are no
# consecutive equal numbers, the array is fully compressed. Repeatedly compress
# until fully compressed.
#
# Example 1: arr = [8, 4, 2, 2, 2, 4] -> [16, 2, 4]
# Example 2: arr = [4, 4, 4, 4] -> [16]
# Example 3: arr = [1, 2, 3, 4] -> [1, 2, 3, 4]
#
# Constraints:
# - len(arr) <= 10^5
# - Each element is a non-negative integer < 10^3