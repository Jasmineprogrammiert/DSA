# compare each day's good/bad flag with the previous day's: if they differ the run extends, else it restarts at 1; track the running max
#
# n: number of days
# T: O(n) — single pass, O(1) work per step
# S: O(1) — a few scalars, nothing grows with n

def longest_alternating(sales):
    if not sales:
        return 0
    r = 1
    longest = streak = 1
    while r < len(sales):
        prev_good = sales[r - 1] >= 10
        cur_good = sales[r] >= 10
        if prev_good != cur_good:
            streak += 1
        else:
            streak = 1
        longest = max(longest, streak)
        r += 1
    return longest

# Alt: same idea as a resetting window — grow while days differ, else reset l past the repeat (r - l is the streak)

def longest_alternating_sequence(sales):
    l, r = 0, 0
    cur_max = 0
    while r < len(sales):
        can_grow = l == r or (sales[r - 1] >= 10) != (sales[r] >= 10)
        if can_grow:
            r += 1
            cur_max = max(cur_max, r - l)
        else:
            l = r
            r += 1
    return cur_max


# # Longest Alternating Sequence

# Given the array `sales`, where `sales[i]` is the number of sales on the `i`-th day, find the longest sequence of days alternating between good days and bad days.

# A _good day_ is a day with at least `10` sales.
# A _bad day_ is a day with fewer than `10` sales.

# Example 1: sales = [8, 9, 20, 0, 9]
# Output: 3. The only good day is day 2, so the subarray [9, 20, 0] alternates from bad to good to bad.

# Example 2: sales = [0, 0, 0]
# Output: 1. Every day is bad, so we cannot find any pair of consecutive days that alternate.

# Example 3: sales = [5, 10, 5, 10]
# Output: 4. The entire array alternates between bad and good days.

# Constraints:

# - `0 <= len(sales) <= 10^5`
# - `0 <= sales[i] <= 10^3`