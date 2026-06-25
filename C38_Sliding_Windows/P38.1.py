# slide a fixed 7-day window across sales, track the max sum
#   add each new day to a running sum
#   when window hits 7 days: update best, then drop the left day
#   return best
# 
# n: number of days in sales
# T: O(n) — one pass; each day is added once and removed once
# S: O(1) — four scalars, no growth with input

def most_weekly_sales(sales):
    l, r = 0, 0
    max_sum, window_sum = 0, 0
    
    while r < len(sales):
        window_sum += sales[r]
        r += 1
        if r - l == 7:
            max_sum = max(max_sum, window_sum)
            window_sum -= sales[l]
            l += 1
    return max_sum


# # Most Weekly Sales

# Given an array, `sales`, find the most sales in any 7-day period.

# Example 1: sales = [0, 3, 7, 12, 10, 5, 0, 1, 0, 15, 12, 11, 1]
# Output: 44
# The 7-day period with the most sales is [5, 0, 1, 0, 15, 12, 11].

# Example 2: sales = [0, 3, 7, 12]
# Output: 0
# There is no 7-day period.

# Example 3: sales = [1, 2, 3, 4, 5, 6, 7]
# Output: 28
# The only 7-day period is the entire array.

# Constraints:

# - The length of `sales` is at most `10^6`
# - Each element in `sales` is a non-negative integer less than `10^3`