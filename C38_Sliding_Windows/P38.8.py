# Sliding window — longest window with <= 3 bad days.
#   grow if next day is good OR window has fewer than 3 bad days
#   shrink otherwise
#   track the longest window length (r - l) seen
#
# n: number of days
# T: O(n) — l and r each advance at most n times
# S: O(1) — a few scalars, nothing grows with n

def max_three_bad_days(sales):
    l, r = 0, 0
    cur_best, bad_days = 0, 0
    while r < len(sales):
        can_grow = sales[r] >= 10 or bad_days < 3
        if can_grow:
            if sales[r] < 10:
                bad_days += 1
            r += 1
            cur_best = max(cur_best, r - l)
        else:
            if sales[l] < 10:
                bad_days -= 1
            l += 1
    return cur_best

# idx:   0 1 2 3
# sales: 5 5 5 5
#  
# l = 1
# r = 4
# bad_days = 3
# cur_best = 3


# # Maximum With At Most 3 Bad Days

# Given an array `sales`, where `sales[i]` is the number of sales on the `i`-th day, find the most consecutive days with at most `3` bad days.

# A _bad day_ is a day with fewer than `10` sales.

# Example 1: sales = [0, 14, 7, 9, 0, 20, 10, 0, 10]
# Output: 6.
# There are two 6-day periods with at most 3 bad days:
#   - [14, 7, 9, 0, 20, 10]
#   - [9, 0, 20, 10, 0, 10]

# Example 2: sales = [10, 10, 10]
# Output: 3. All days are good days.

# Example 3: sales = [5, 5, 5, 5]
# Output: 3. We can include at most 3 bad days.

# Constraints:

# - `0 <= len(sales) <= 10^5`
# - `0 <= sales[i] <= 10^3`