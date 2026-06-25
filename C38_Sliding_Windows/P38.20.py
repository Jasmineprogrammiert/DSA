# An array of length n has n*(n+1)/2 non-empty subarrays
# "At least k bad days" covers k, k+1, k+2, ... bad days
# So: (subarrays with >= k bad days) = (all subarrays) - (subarrays with <= k-1 bad days)

# n: number of days
# T: O(n) — l and r each only move forward
# S: O(1) — a few scalars

def count_subarrays(sales, k):
    n = len(sales)
    total_subarr = n * (n + 1) // 2
    if k == 0:
        return total_subarr
    return total_subarr - at_most(sales, k - 1)

def at_most(sales, k):
    l, r = 0, 0
    bad = 0
    count = 0
    while r < len(sales):
        can_grow = bad < k or sales[r] >= 10
        if can_grow:
            if sales[r] < 10:
                bad += 1
            r += 1
            count += r - l
        else:
            if sales[l] < 10:
                bad -= 1
            l += 1
    return count


# # Count Subarrays With At Least K Bad Days

# Given an array, `sales`, where `sales[i]` is the number of sales on day `i`, count the number of subarrays with at least `k` bad days.

# A _bad day_ is a day with fewer than 10 sales.

# Example 1: sales = [0, 20, 5], k = 1
# Output: 5
#   - the subarrays [0], [0, 20], [20, 5], and [5] have 1 bad day each
#   - [0, 20, 5] has 2 bad days

# Example 2: sales = [10, 20, 30], k = 1
# Output: 0
# No subarrays have any bad days.

# Example 3: sales = [0, 5, 8], k = 2
# Output: 3
# The subarrays [0, 5], [5, 8], and [0, 5, 8] have at least 2 bad days.

# Constraints:

# - `0 <= sales.length <= 10^5`
# - `0 <= sales[i] < 10^3`
# - `0 <= k <= 10^5`