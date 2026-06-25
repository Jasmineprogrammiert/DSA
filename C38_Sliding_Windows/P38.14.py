# variable-length sliding window: shrink while the window is "good enough"
# grow right while total <= 20 (not yet over the threshold)
# once total > 20 the window qualifies -> record its length, then shrink from the left
#   to look for a shorter qualifying window
# stop when the right end runs off and the window still isn't over 20

# n: length of sales
# T: O(n) — l and r each only move forward, at most n steps total
# S: O(1) — only running counters

def shortest_period(sales):
    l, r = 0, 0
    total, shortest = 0, float('inf')
    while True:
        if total <= 20:
            if r == len(sales):
                break
            total += sales[r]
            r += 1
        else:
            shortest = min(shortest, r - l)
            total -= sales[l]
            l += 1
    return shortest if shortest != float('inf') else -1


# # Shortest Period With Over 20 Sales

# Given an array, `sales`, where `sales[i]` is the number of sales on day `i`, find the shortest period of time with over 20 sales, or `-1` if there isn't any.

# Example 1: sales = [5, 10, 15, 5, 10]
# Output: 2. The subarray [10, 15] has over 20 sales.

# Example 2: sales = [5, 10, 4, 5, 10]
# Output: 4. [5, 10, 4, 5] and [10, 4, 5, 10] have over 20 sales.

# Example 3: sales = [5, 5, 5, 5]
# Output: -1. There is no subarray with more than 20 sales.

# Constraints:

# - `0 <= len(sales) <= 10^5`
# - `0 <= sales[i] <= 10^3`