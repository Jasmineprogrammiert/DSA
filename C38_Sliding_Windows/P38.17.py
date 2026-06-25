# Reframe: find the smallest window holding (B - k) bad days, flip every bad day outside it
# This maximizes the combined prefix + suffix of good days; B is the total bad days

# n: length of projected_sales
# T: O(n) — one sum pass plus a two-pointer loop where l, r only advance (≤ 2n steps)
# S: O(1) — scalar counters only

def strong_days(projected_sales, k):
    n = len(projected_sales)
    total_bad = sum(s < 10 for s in projected_sales)
    target = total_bad - k
    if target <= 0:
        return n
    
    l, r = 0, 0
    shortest = float('inf')
    bad_in_win = 0
    while True:
        must_grow = bad_in_win < target
        if must_grow:
            if r == n:
                break
            if projected_sales[r] < 10:
                bad_in_win += 1
            r += 1
        else:
            shortest = min(shortest, r - l)
            if projected_sales[l] < 10:
                bad_in_win -= 1
            l += 1
    return n - shortest


# # Strong Start And Ending

# Imagine that you have a little bookstore. We have an array, `projected_sales`, with the projected number of sales per day of the fall season.

# We would like to start and close the season strong. We want to have as many consecutive _good_ days as possible starting from day `0` and as many consecutive _good_ days as possible ending on the last day.

# A _good_ day is a day with at least `10` sales.

# We can pick `k` days to boost with advertising, which we expect to boost the sales on those specific days by at least `20`. What's the maximum number of combined initial good days and final good days we can have?

# Example 1: projected_sales = [10, 0, 0, 0, 10, 0, 0, 10], k = 2
# Output: 5
# We should boost days 5 and 6 so that the projected sales after boosting are:
#     [10, 0, 0, 0, 10, 20, 20, 10]
# This way, we have 1 initial and 4 final good days.

# Example 2: projected_sales = [0, 10, 0, 10], k = 1
# Output: 3
# It does not matter which day you boost.

# Example 3: projected_sales = [5, 5, 5], k = 2
# Output: 2
# We can boost any two days.

# Constraints:

# - `0 <= len(projected_sales) <= 10^5` (the bookstore is in a fictional world with very long fall seasons)
# - `0 <= projected_sales[i] <= 10^3`
# - `0 <= k <= 10^5`