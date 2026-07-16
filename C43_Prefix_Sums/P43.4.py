# # Pattern — Left/Right Split via Running Total
# Use when you compare sum-of-left vs sum-of-right around each index i.
# Key identity (right is derived, not tracked):
#   right(i) = total - left(i) - arr[i]        total = sum(arr); pivot joins neither side
# Sweep once, keeping left as a running prefix; test the balance condition.
#   -> left starts at 0; add arr[i] to left AFTER testing index i.
#
# n: length of arr
# T: O(n) — one pass for sum(arr), one sweep with O(1) work per index
# S: O(1) extra — just total and left; right is derived, never stored

def balance_index(arr):
    total = sum(arr)
    left = 0

    for i in range(len(arr)):
        right = total - left - arr[i]
        if left == right:
            return i
        left += arr[i]
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