# 0, 1  2  3   4        INDEX
# 1, 2, 3, -2, 1        ARR
#              r
# max_sum = max(max_sum, sum)
#         = 6
# sum     = 5


# 0, 1  2  3   4        INDEX
# 1, 2, 3, -8, 7        ARR
#                 r
# max_sum = max(max_sum, sum)
#         = 7
# sum     = 7
# advance r if win_sum + arr[r] >= 0, otherwise reset the window

# n: length of arr
# T: O(n) - each element is iterated once by r
# S: O(1) - only three variables are used regardless of input size

def max_subarr_sum(arr):
    max_sum = max(arr)
    win_sum = 0
    r = 0

    while r < len(arr):
        if win_sum + arr[r] >= 0:
            win_sum += arr[r]
            max_sum = max(max_sum, win_sum)
        else:
            win_sum = 0
        r += 1
    return max_sum


# # Max Subarray Sum

# Given a non-empty array `arr` of integers (which can be negative), find the non-empty subarray with the maximum sum and return its sum.

# Example 1: arr = [1, 2, 3, -2, 1]
# Output: 6. The subarray with the maximum sum is [1, 2, 3].

# Example 2: arr = [1, 2, 3, -2, 7]
# Output: 11. The subarray with the maximum sum is the whole array.

# Example 3: arr = [1, 2, 3, -8, 7]
# Output: 7. The subarray with the maximum sum is [7].

# Example 4: arr = [-2, -3, -4]
# Output: -2. The subarray cannot be empty.

# Constraints:

# - `1 <= len(arr) <= 10^5`
# - Each element in `arr` is an integer between `-10^6` and `10^6`