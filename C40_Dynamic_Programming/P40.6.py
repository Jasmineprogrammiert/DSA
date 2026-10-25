# dp[elem]: minimum operations to reduce elem to 1
# elem         1 2 3 4 5 6 7 8 9 10
# dp[elem]     0 1 1 2 3 2 3 3 2 3

# n: starting number
# T: O(n) - process 2 through n, checking at most 3 options each
# S: O(n) - dp stores n + 1 operation counts

def min_step_to_one(n):
    dp = [0] * (n + 1)
    for elem in range(2, n + 1):
        dp[elem] = 1 + dp[elem - 1]
        if elem % 2 == 0:
            dp[elem] = min(dp[elem], 1 + dp[elem // 2])
        if elem % 3 == 0:
            dp[elem] = min(dp[elem], 1 + dp[elem // 3])
    return dp[n]


# # Minimum Steps to One

# Write a function that accepts a positive integer, `n`, and returns the minimum number of operations to get to `1`, assuming we can choose between the following operations:

# - Subtract `1`.
# - Divide by `2`. We can only do this if the number is divisible by `2`.
# - Divide by `3`. We can only do this if the number is divisible by `3`.

# Example 1:
# n = 10
# Output: 3. We can do 10 -> 9 -> 3 -> 1.

# Example 2:
# n = 1
# Output: 0

# Example 3:
# n = 15
# Output: 4

# Constraints:

# - `n` is at least `1` and at most `10^6`.