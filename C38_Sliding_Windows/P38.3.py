# same fixed-window skeleton as P38.1, but a freq_map maintains the window's title counts
# window full (r - l == k): len(freq_map) == k → all k distinct → True, else False
#
# n: number of days   
# k: window width
# T: O(n) — each day enters and leaves the window once
# S: O(k) — freq_map holds at most k titles

from collections import defaultdict


def unique_best_seller_streak(best_seller, k):
    l, r = 0, 0
    freq_map = defaultdict(int)
    while r < len(best_seller):
        freq_map[best_seller[r]] += 1
        r += 1
        if r - l == k:
            if len(freq_map) == k:
                return True
            freq_map[best_seller[l]] -= 1
            if freq_map[best_seller[l]] == 0:
                del freq_map[best_seller[l]] 
            l += 1
    return False


# # Unique Best Seller Streak

# We are given an array, `best_seller`, with the title of the most sold book for each day over a given period. We are also given a number `k` with `1 ≤ k ≤ len(sales)`.

# We need to return whether there is any k-day period where each day has a **different** best-selling title.

# Example 1:
# best_seller = ["book3", "book1", "book3", "book3", "book2", "book3", "book4", "book3"]
# k = 3

# Output: True
# There is a 3-day period without a repeated value: ["book2", "book3", "book4"]

# Example 2:
# best_seller = ["book3", "book1", "book3", "book3", "book2", "book3", "book4", "book3"]
# k = 4

# Output: False
# There are no 4-day periods without a repeated value

# Example 3:
# best_seller = ["book1", "book2", "book3"]
# k = 3

# Output: True
# The entire array has no repeated values

# Constraints:

# - The length of `best_seller` is at most `10^6`
# - Each book title has length at most `100`
# - `1 <= k <= len(best_seller)`