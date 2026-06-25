# Reframing the problem: look for the longest window with at most k bad days, 
# cuz we can pick those bad days and turn them into good days
#
# n: number of days
# T: O(n) — l and r each advance at most n times
# S: O(1) — a few scalars, nothing grows with n

def ad_campaign(projected_sales, k):
    l, r = 0, 0
    cur_best, bad_days = 0, 0
    while r < len(projected_sales):
        can_grow = projected_sales[r] >= 10 or bad_days < k
        if can_grow:
            if projected_sales[r] < 10:
                bad_days += 1
            r += 1
            cur_best = max(cur_best, r - l)
        else:
            if projected_sales[l] < 10:
                bad_days -= 1
            l += 1
    return cur_best


# # Ad Campaign Boost

# Imagine that you have a little bookstore. We have an array, `projected_sales`, with the projected number of sales per day in the future.

# We are trying to pick `k` days for an advertising campaign, which we expect to boost the sales on those specific days by at least `20`.

# If we pick the days for the advertising campaign correctly, what is the maximum number of consecutive good days in a row we can get?

# A _good day_ is a day with at least `10` sales.

# Example 1: projected_sales = [5, 0, 20, 0, 5], k = 2
# Output: 3.
# The only good day is day 2. We can boost:
#   - days 0 and 1,
#   - days 1 and 3, or
#   - days 3 and 4.
# For instance, if we boost days 0 and 1, the projected sales become:
# [25, 20, 20, 0, 5], with 3 consecutive good days.

# Example 2: projected_sales = [0, 10, 0, 10], k = 1
# Output: 3. We can boost day 2; boosting day 0 is suboptimal.

# Example 3: projected_sales = [5, 5, 5], k = 3
# Output: 3. We can boost all days to make them good days.

# Constraints:

# - `1 <= k <= len(projected_sales) <= 10^5`
# - `0 <= projected_sales[i] <= 10^3`