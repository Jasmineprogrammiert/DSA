# Find the longest window with at most k bad days
# Each time r advances by one, every subarray ending at r-1 with left ≥ l is valid, so add r - l

# n: length of sales
# T: O(n) — single loop, l and r move forward only (≤ 2n steps)
# S: O(1) — scalar counters only

def count_subarrays(sales, k):
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


# # Count Subarrays With At Most K Bad Days

# Given an array, `sales`, where `sales[i]` is the number of sales on day `i`, count the number of subarrays with at most `k` bad days.

# A _bad day_ is a day with fewer than 10 sales.

# Example 1: sales = [0, 20, 5], k = 1
# Output: 5
#   - [20] has 0 bad days
#   - [0], [0, 20], [20, 5], and [5] have 1 bad day each

# Example 2: sales = [10, 20, 30], k = 1
# Output: 6
# All subarrays have 0 bad days

# Example 3: sales = [0, 5, 8], k = 1
# Output: 3
# Only [0], [5], and [8] have at most 1 bad day

# Constraints:

# - `0 <= sales.length <= 10^5`
# - `0 <= sales[i] < 10^3`
# - `0 <= k <= 10^5`