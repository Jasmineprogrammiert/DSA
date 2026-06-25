# Same window skeleton as P38.11, but the limit is "<= k distinct titles", not "<= k boosts":
#   - validity is a freq map of titles, not a running cost scalar
#   - can grow if title is a repeat (free) or there's room for a new one (distinct < k)
#   - shrinking must delete a title's key when its count hits 0, not just subtract a cost
#   - k >= 1 -> any single title fits, so P38.11's empty-window (l == r) guard isn't needed
#
# n: number of days
# T: O(n) — each index enters via r once and leaves via l at most once;
#           titles are <= 100 chars, so hashing is O(1)
# S: O(k) — the window holds at most k distinct titles at any moment

from collections import defaultdict


def max_at_most_k_distinct(best_seller, k):
    l, r = 0, 0
    longest = 0
    window_counts = defaultdict(int)

    while r < len(best_seller):
        title = best_seller[r]
        can_grow = title in window_counts or len(window_counts) < k

        if can_grow:
            window_counts[title] += 1
            r += 1
            longest = max(longest, r - l)
        else:
            left = best_seller[l]
            window_counts[left] -= 1
            if window_counts[left] == 0:
                del window_counts[left]
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