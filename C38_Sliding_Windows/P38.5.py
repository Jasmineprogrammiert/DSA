# a good-day streak only grows or fully resets - track length directly, no left pointer needed
# prefer the streak counter - l/r window works too, but tracks positions to derive a length you never actually need


# ---- 1. streak counter ----

# n: length of sales
# T: O(n) - single pass
# S: O(1) - only two vars used regardless of input size

def longest_streak(sales):
    streak, longest = 0, 0
    r = 0
    while r < len(sales):
        if sales[r] >= 10:
            streak += 1
            longest = max(longest, streak)
        else:
            streak = 0
        r += 1
    return longest


# ---- 2. l/r window ----

# 0 1  2 3  4  5        INDEX
# 0 14 7 12 10 20       SALES
#        l
#                 r
# cur_best = max(cur_best, r - l) = 3

# n: length of sales
# T: O(n) - single pass; l is reassigned on a bad day instead of iterating
# S: O(1) - only three vars used regardless of input size

def longest_streak_lr(sales):
    l, r = 0, 0
    cur_best = 0

    while r < len(sales):
        if sales[r] < 10:
            r += 1
            l = r
        else:
            r += 1
            cur_best = max(cur_best, r - l)
    return cur_best


# # Longest Good Day Streak

# Given an array, `sales`, where `sales[i]` is the number of sales on the `i`-th day, find the most consecutive days with no bad days.

# A _bad day_ is a day with fewer than `10` sales.

# Example 1: sales = [0, 14, 7, 12, 10, 20]
# Output: 3. The subarray [12, 10, 20] has no bad days.

# Example 2: sales = [10, 10, 10]
# Output: 3. All days are good days.

# Example 3: sales = [5, 5, 5]
# Output: 0. There are no good days.

# Constraints:

# - `0 <= len(sales) <= 10^5`
# - `0 <= sales[i] <= 10^3`