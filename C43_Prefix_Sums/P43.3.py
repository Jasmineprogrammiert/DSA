# Problem 43.3 - Exclusive Product
# Given an array of non-negative integers, arr, return an array with the
# same length where index i contains the product of all the elements in arr
# except arr[i]. Since the values could be very large, return them modulo
# 10^9 + 7.
#
# Note: The "obvious" division approach doesn't work because modulo and
# division don't commute: (12 / 3) % 5 != (12 % 5) / 3. Solve without
# division.
#
# Example 1: arr = [1, 3, 2, 1] -> [6, 2, 3, 6]
# Example 2: arr = [0, 1, 0] -> [0, 0, 0]
#
# Constraints:
# - 0 <= arr[i] <= 10000
# - 2 <= len(arr) <= 10^6