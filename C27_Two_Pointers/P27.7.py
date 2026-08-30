# sorted arr > inward pointers

# n: length of array
# T: O(n) - each element is visited once
# S: O(1) - only using constant extra space for the two pointers

# arr = [-3, 0, 0, 1, 2]
# index   0   1  2  3  4
#      arr[l]  arr[r]  total
#       -3       2      -1
#        0              2
#                1      1
#                0      0

def two_sum(arr):
    l, r = 0, len(arr) - 1
    
    while l < r:
        total = arr[l] + arr[r]
        if total == 0:
            return True
        elif total > 0:
            r -= 1
        else:
            l += 1
    return False


# # Two Sum

# Given a sorted array of integers, `arr`, return whether there are two _distinct_ indices, `i` and `j`, such that `arr[i] + arr[j] = 0`.

# Example 1:
# Input: arr = [-5, -2, -1, 1, 1, 10]
# Output: true
# Explanation: The elements -1 and 1 sum to zero.

# Example 2:
# Input: arr = [-3, 0, 0, 1, 2]
# Output: true
# Explanation: The two 0s sum to zero.

# Example 3:
# Input: arr = [-5, -3, -1, 0, 2, 4, 6]
# Output: false
# Explanation: No two elements sum to zero.

# Constraints:

# - arr is sorted in ascending order
# - 0 ≤ arr.length ≤ 10^6
# - -10^9 ≤ arr[i] ≤ 10^9