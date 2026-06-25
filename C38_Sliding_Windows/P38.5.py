# a good-day streak is a run that only grows or fully resets — track its length, no left pointer
#   walk r across sales, classifying each day (good = sales[r] >= 10)
#   good day: extend the current run (streak += 1), then update the best seen
#   bad day: the run is broken, reset streak to 0
#   return the longest run found
#
# n: number of days
# T: O(n) — single pass, constant work per day
# S: O(1) — just streak, longest, and r

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