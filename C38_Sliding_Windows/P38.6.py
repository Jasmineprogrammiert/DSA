# Kadane via window: drop the prefix the moment it would turn the running sum negative (it can only hurt later sums); seed max_sum with max(arr) to cover the all-negative case
#
# n: length of arr
# T: O(n) — single pass (plus one O(n) max for the seed)
# S: O(1) — only max_sum, window_sum, r

def max_subarr_sum(arr):
    max_sum = max(arr)
    if max_sum <= 0:
        return max_sum
    window_sum = 0
    r = 0
    while r < len(arr):
        if window_sum + arr[r] >= 0:
            window_sum += arr[r]
            max_sum = max(max_sum, window_sum)
        else:
            window_sum = 0
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