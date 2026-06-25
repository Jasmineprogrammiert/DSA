# A range [k1, k2] = atMost(k2) − atMost(k1 − 1), reusing the atMost helper (see 38.18–38.20)
# Special-case k1 == 0, since atMost(−1) would wrongly count instead of returning 0
#
# n: length of sales
# T: O(n) — atMost advances two forward-only pointers, n steps each; called a constant number of times
# S: O(1) — a handful of scalar counters, no auxiliary structure

def count_subarrays(sales, k1, k2):
    if k1 == 0:
        return at_most(sales, k2)
    return at_most(sales, k2) - at_most(sales, k1 - 1)

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


# # Count Subarrays With Bad Days In Range

# We are given an array, `sales`, where `sales[i]` is the number of sales on day `i`. We are also given two numbers, `k1` and `k2`, with `0 ≤ k1 ≤ k2`.

# Count the number of subarrays with at least `k1` bad days and at most `k2` bad days.

# A _bad day_ is a day with fewer than 10 sales.

# Example 1: sales = [0, 20, 5], k1 = 2, k2 = 2
# Output: 1
# The subarray [0, 20, 5] has 2 bad days.

# Example 2: sales = [0, 20, 5], k1 = 1, k2 = 2
# Output: 5
# - The subarray [0, 20, 5] has 2 bad days.
# - The subarrays [0], [0, 20], [20, 5], and [5] have 1 bad day.

# Example 3: sales = [10, 20, 30], k1 = 1, k2 = 2
# Output: 0
# No subarrays have any bad days.

# Constraints:

# - `0 <= sales.length <= 10^5`
# - `0 <= sales[i] <= 10^3`
# - `0 <= k1 <= k2 <= 10^5`