# same fixed-window skeleton as P38.1, but track a running sum + the best window's start
# window full (r - l == k): sum beats best → record sum + start l (strict > keeps first on ties)
#
# n: number of days
# T: O(n) — each day enters and leaves the window once
# S: O(1) — scalars only, no growth with input

def most_sales(sales, k):
    l, r = 0, 0
    cur_best, window_sum, first_d = 0, 0, 0
    while r < len(sales):
        window_sum += sales[r]
        r += 1
        if r - l == k:
            if cur_best < window_sum:
                cur_best = window_sum
                first_d = l
            window_sum -= sales[l]
            l += 1
    return first_d


# # Most Sales In K Days

# Given the array `sales` and a number `k` with `1 ≤ k ≤ len(sales)`, find the most sales in any k-day period.

# Return the first day of that period (days start at `0`). If there are multiple k-day periods with the most sales, return the first day of the first one.

# Example 1: sales = [8, 1, 3, 7], k = 2
# Output: 2
# The subarray of length 2 with maximum sum is [3, 7], which starts at index 2.

# Example 2: sales = [5, 10, 15, 5], k = 1
# Output: 2
# The day with most sales is day 2 with 15 sales.

# Example 3: sales = [1, 2, 3], k = 3
# Output: 0
# The only valid period is the entire array.

# Constraints:

# - The length of `sales` is at most `10^6`
# - Each element in `sales` is a non-negative integer less than `10^3`
# - `1 ≤ k ≤ len(sales)`