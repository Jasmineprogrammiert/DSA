# eager      predict before the add: can the window take best_seller[r] and stay valid?
# lazy       add, then repair: while the window is invalid, evict from the left
#            prefer lazy - no prediction to get wrong, and l is free to catch up to r


# ---- 1. lazy: add, then repair ----

# move r every pass,
# move l while the window HOLDS more than k distinct titles

# n: length of best_seller
# k: max distinct titles
# T: O(n) - each title enters and leaves the window once
# S: O(k) - the dict holds at most k + 1 titles, between the add and the repair

from collections import defaultdict

def max_at_most_k_distinct_lazy(best_seller, k):
    l, r = 0, 0
    longest = 0
    freq_map = defaultdict(int)

    while r < len(best_seller):
        freq_map[best_seller[r]] += 1
        r += 1

        while len(freq_map) > k:
            left = best_seller[l]
            freq_map[left] -= 1
            if freq_map[left] == 0:
                del freq_map[left]
            l += 1

        longest = max(longest, r - l)
    return longest


# ---- 2. eager: predict before adding ----

# move r to grow the window,
# move l when the window would hold more than k distinct titles
#
# len(freq_map) < k     there is room for a NEW title
# title in freq_map     already counted, so it costs no room

# S: O(k) - the dict doesn't hold more than k titles

# k = 2             AT MOST 2 DISTINCTS
# 0 1 2 3 4 5       INDEX
# 1 1 2 1 3 1       ARR
#       l
#             r
# longest = 4
# freq_map = {1: 2, 3: 1}

def max_at_most_k_distinct(best_seller, k):
    l, r = 0, 0
    longest = 0
    freq_map = defaultdict(int)

    while r < len(best_seller):
        title = best_seller[r]
        can_grow = len(freq_map) < k or title in freq_map
        if can_grow:
            freq_map[title] += 1
            r += 1
            longest = max(longest, r - l)
        else:
            left = best_seller[l]
            freq_map[left] -= 1
            if freq_map[left] == 0:
                del freq_map[left]
            l += 1
    return longest


# # Longest Period At Most K Distinct

# We are given an array of strings, `best_seller`, where `best_seller[i]` is the title of
# the most sold book for day `i`, and a number `k >= 1`.

# Find the maximum consecutive days with at most `k` **distinct** best-selling books.

# Example 1:
# best_seller = ["book1", "book1", "book2", "book1", "book3", "book1"]
# k = 2
# Output: 4
# The subarray ["book1", "book1", "book2", "book1"] contains only 2 distinct titles

# Example 2:
# best_seller = ["book1", "book2", "book3"]
# k = 1
# Output: 1
# Each day has a different best seller

# Example 3:
# best_seller = ["book1", "book1", "book1"]
# k = 2
# Output: 3
# The entire array has only 1 distinct title

# Constraints:
# - 0 <= len(best_seller) <= 10^6
# - 1 <= k <= len(best_seller)
# - 1 <= len(best_seller[i]) <= 100