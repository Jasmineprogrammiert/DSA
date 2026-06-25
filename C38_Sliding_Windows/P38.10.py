# Reframe: longest window with <= k values in [5, 9] and 0 values < 5
#   >= 10 -> already good (free) | 5..9 -> boostable (costs 1 of k) | < 5 -> wall (reset window)
#
# n: number of days
# T: O(n) — l and r each only move forward
# S: O(1) — a few scalars

def ad_campaign(projected_sales, k):
    l, r = 0, 0
    longest, boosts_used = 0, 0
    while r < len(projected_sales):
        val = projected_sales[r]
        can_grow = val >= 10 or (5 <= val <= 9 and boosts_used < k)
        if can_grow:
            if 5 <= val <= 9:
                boosts_used += 1
            r += 1
            longest = max(longest, r - l)
        elif val < 5:
            l = r + 1
            r += 1
            boosts_used = 0
        else:
            if 5 <= projected_sales[l] <= 9:
                boosts_used -= 1
            l += 1
    return longest


# # Ad Campaign With Small Boosts

# Imagine that you have a little bookstore. We have an array, `projected_sales`, with the projected number of sales per day in the future.

# We are trying to pick `k` days for an advertising campaign, which we expect to boost the sales on those specific days by `5` sales. **You cannot boost the same day more than once.**

# If we pick the days for the advertising campaign correctly, what is the maximum number of consecutive good days in a row we can get?

# A _good day_ is a day with at least `10` sales.

# Example 1: projected_sales = [8, 4, 8], k = 3
# Output: 1. We can boost all 3 days, resulting in [13, 9, 13] projected sales.
# The max consecutive good days is 1.

# Example 2: projected_sales = [10, 5, 8], k = 1
# Output: 2. We should boost day 1, resulting in [10, 10, 8] projected sales.

# Example 3: projected_sales = [8, 8, 8], k = 3
# Output: 3. We can boost all days to reach 13 sales each.

# Constraints:

# - `0 <= len(projected_sales) <= 10^5`
# - `0 <= projected_sales[i] <= 10^3`
# - `0 <= k <= len(projected_sales)`