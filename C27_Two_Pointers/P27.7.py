# create two pointers moving inward
# l moves from left to right, r moves from right to left
# arr[l] is smaller than 0, arr[r] is larger or equal to 0. This limites the bound of l and r
# when arr[l] adn arr[r] is larger than 0, arr[r] is too large, so move r one index to the left
# when arr[l] adn arr[r] is smaller than 0, arr[l] is too large, so move l one index to the right
# when their sum equal to 0, return True

def two_sum(arr):
    l, r = 0, len(arr) - 1
    
    while l < r:
        if arr[l] + arr[r] > 0:
            r -= 1
        elif arr[l] + arr[r] < 0:
            l += 1
        else:
            return True
    return False
    
# n: sum of all array length
# T: O(n) - each element is visited once
# S: O(1) - only using constant extra space for the two pointers



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