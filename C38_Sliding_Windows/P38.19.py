# Exactly k = At most k - At most (k-1)         REFRAME
# move r every pass,
# move l when the window holds more than k bad days
# BAD_DAY < 10, k = 1

# 0 1  2        INDEX
# 0 20 5        ARR
#   l
#         r
# bad_d = 1
# at_most_k = 5

# n: length of sales
# T: O(n) - each element is visited at most twice, O(2n) -> O(n)
# S: O(1) - 4 vars are used regardless on the arr size

def count_subarr(sales, k):
    def at_most(k):
        l, r = 0, 0
        bad_d = 0
        at_most_k = 0

        while r < len(sales):
            if sales[r] < 10:
                bad_d += 1
            r += 1
            
            while bad_d > k:
                if sales[l] < 10:
                    bad_d -= 1
                l += 1
            
            at_most_k += r - l
        return at_most_k
    
    if k == 0:
        return at_most(0)
    return at_most(k) - at_most(k - 1)


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