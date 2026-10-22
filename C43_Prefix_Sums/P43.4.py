# 0  1  2  3  4  5  6        IDX
# 3  5 -2  7  2  2  2        ARR
# 0  3  8  6                 L
#          i

# i = 3
# r = total - l - arr[i] = 19 - 6 - 7 = 6
# total = 19

# return the first _balanced index_, if there is any, or `-1` otherwise
# the sum of the elements to its left is the same as the sum of the elements to its right

# n: length of arr
# T: O(n) - one pass for the total, then one pass to find the balance point
# S: O(1) - a fixed number of variables

def balance_point(arr):
    total = sum(arr)
    l = 0

    for i in range(len(arr)):
        r = total - l - arr[i]
        if l == r:
            return i
        l += arr[i]
    return -1


# # Balance Point

# Given an array of integers, `arr`, return the first _balanced index_, if there is any, or `-1` otherwise. An index is balanced if the sum of the elements to its left is the same as the sum of the elements to its right.

# Example:
# arr = [3, 5, -2, 7, 2, 2, 2]
# Output: 3
# Index 3 is balanced because 3 + 5 + (-2) equals 2 + 2 + 2.

# Constraints:

# - The length of `arr` is at most `10^5`
# - Each element in `arr` is an integer at most `10^4`