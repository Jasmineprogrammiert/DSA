# A subarray is valid iff it starts and ends on a good day
# Over a list of just the good days, every subarray has good start and end
# An array of length n has n*(n+1)/2 non-empty subarrays
# Thus the answer is n*(n+1)/2, where n is the number of good days in sales
# 
# n: number of days
# T: O(n) — scan every day once to count good days
# S: O(1) — a single running count; the generator streams

def count_subarrays(sales):
    good_days = sum(1 for x in sales if x >= 10)
    return good_days * (good_days + 1) // 2


# # Count Subarrays With Good Start And Ending

# Given an array, `sales`, where `sales[i]` is the number of sales on day `i`, return the number of subarrays that start and end on a good day.

# A _good day_ is a day with at least 10 sales.

# Example 1: sales = [0, 20, 5, 15, 10]
# Output: 6
# The good days are at indices 1, 3, and 4
# The valid subarrays are:
# - [20]
# - [15]
# - [10]
# - [20, 5, 15]
# - [15, 10]
# - [20, 5, 15, 10]

# Example 2: sales = [0, 5, 8]
# Output: 0
# There are no good days.

# Example 3: sales = [10, 20, 30]
# Output: 6
# All days are good, so all subarrays count.

# Constraints:

# - `0 <= sales.length <= 10^5`
# - `0 <= sales[i] < 10^3`