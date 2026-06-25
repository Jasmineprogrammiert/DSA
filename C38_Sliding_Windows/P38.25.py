# Valid subarrays can't span a bad day (sales < 10), so split into
# maximal good-day segments and count within each independently
#
# 1. Resetting window to find the maximal good-day segments:
#    on a bad day, reset left pointer + running sum past it.
# 2. Within a segment (all elements > 0, so window sum is monotonic),
#    count subarrays with sum >= k via complement:
#       >= k  = total  -  at_most_k(k - 1)
#       total = n(n + 1) / 2     # n = array length
#
# n: length of sales
# T: O(n) — good_subarr scans once; at_most_k runs two forward-only pointers per good run, and the run lengths sum to n
# S: O(n) — good_subarr stores each good run as a slice, copying each good day once (O(1) if we pass indices instead of slicing)

def count_good_subarr(sales, k):
    def good_subarr(arr):
        l, r = 0, 0
        subarr = []
        while r < len(arr):
            if arr[r] >= 10:
                r += 1
            else:
                if r > l: # rejecting r == l case
                    subarr.append(arr[l: r])
                r += 1
                l = r
        if r > l:
            subarr.append(arr[l: r])
        return subarr
    
    def at_most_k(arr, k):
        l, window_sum, count = 0, 0, 0
        for r in range(len(arr)):
            window_sum += arr[r]
            while window_sum > k:
                window_sum -= arr[l]
                l += 1
            count += r - l + 1
        return count
    
    res = 0
    for arr in good_subarr(sales):
        n = len(arr)
        total = n * (n + 1) // 2
        res += total - at_most_k(arr, k - 1)
    return res
    

# # Count Good Subarrays With At Least K Sales

# You are given an array, `sales`, where `sales[i]` is the number of sales on day `i`, and a positive number `k`.

# Return the number of subarrays with no bad days and at least `k` total sales.

# A _bad day_ is a day with fewer than `10` sales.

# Example 1: sales = [15, 20, 5, 30, 25], k = 50
# Output: 1
# The only subarray with no bad days and at least 50 total sales is:
#   - [30, 25]

# Example 2: sales = [10, 20, 30], k = 40
# Output: 2
# There are no bad days. The subarrays with at least 40 total sales are:
#   - [10, 20, 30]
#   - [20, 30]

# Example 3: sales = [0, 5, 8], k = 10
# Output: 0
# All days are bad days.

# Constraints:

# - `0 <= sales.length <= 10^5`
# - `0 <= sales[i] <= 10^3`
# - `1 <= k <= 10^7`