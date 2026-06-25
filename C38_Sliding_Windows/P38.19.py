# Exactly k bad days = (at most k) - (at most k-1)
# at_most: longest-window two-pointer; each grow adds r - l valid subarrays

# n: length of sales
# T: O(n) — at_most moves l and r forward only (≤ 2n moves), O(1) work each; called twice → still O(n)
# S: O(1) — fixed scalar variables, no extra structures

def count_subarrays(sales, k):
    if k == 0:
        return at_most(sales, 0)
    return at_most(sales, k) - at_most(sales, k - 1)

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


# # Count Subarrays With Exactly K Bad Days

# Given an array, `sales`, where `sales[i]` is the number of sales on day `i`, count the number of subarrays with exactly `k` bad days.

# A _bad day_ is a day with fewer than 10 sales.

# Example 1: sales = [0, 20, 5], k = 1
# Output: 4
# The subarrays [0], [0, 20], [20, 5], and [5] have 1 bad day each.

# Example 2: sales = [10, 20, 30], k = 1
# Output: 0
# No subarrays have exactly 1 bad day.

# Example 3: sales = [0, 5, 8], k = 2
# Output: 2
# The subarrays [0, 5] and [5, 8] have exactly 2 bad days.

# Constraints:

# - `0 <= sales.length <= 10^5`
# - `0 <= sales[i] < 10^3`
# - `0 <= k <= 10^5`