# Reframe: the cost of turning a day with x sales into a good day is max(10-x, 0)
# 
# n: number of days
# T: O(n) — l and r each only move forward
# S: O(1) — a few scalars

def boosting_days(projected_sales, k):
    l, r = 0, 0
    longest, boosts_used = 0, 0
    while r < len(projected_sales):
        val = projected_sales[r]
        can_grow = max(10 - val, 0) + boosts_used <= k
        if can_grow:
            boosts_used += max(10 - val, 0)
            r += 1
            longest = max(longest, r - l)
        elif l == r:
            r += 1
            l = r
        else:
            boosts_used -= max(10 - projected_sales[l], 0)
            l += 1
    return longest


# # Boosting Days Multiple Times

# Imagine that you have a little bookstore. We have an array, `projected_sales`, with the projected number of sales per day in the future.

# We are doing an advertising campaign and have a total of `k` boosts that we can use on any of the days. We expect each boost to increase the sales on the chosen day by `1`. **You can boost the same day multiple times.**

# If we use the boosts correctly, what is the maximum number of consecutive good days in a row we can get?

# A _good day_ is a day with at least `10` sales.

# Example 1: projected_sales = [5, 5, 15, 0, 10], k = 12
# Output: 3
# We can reach 3 consecutive good days in two ways:
#   - boosting days 0 and 1 to reach 10 sales each, or
#   - boosting day 3 to reach 10 sales.

# Example 2: projected_sales = [5, 5, 15, 0, 10], k = 15
# Output: 4
# We can boost days 1 and 3 to reach 10 sales each.

# Example 3: projected_sales = [0, 0, 0], k = 29
# Output: 2
# We can use all boosts on days 0 and 1 to reach 10 sales each.

# Constraints:

# - `0 <= len(projected_sales) <= 10^5`
# - `0 <= projected_sales[i] <= 10^3`
# - `0 <= k <= 10^7`