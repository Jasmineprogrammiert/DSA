# better space: no freq_map needed — a same-title run is contiguous, so anchor l at the run's start and let r extend it; reset l = r on a mismatch. Run length hitting k ⇒ True
#
# n: number of days
# k: window width
# T: O(n) — each day visited once
# S: O(1) — just pointers/counters, no map

def best_seller_streak(best_seller, k):
    streak = 0
    l, r = 0, 0
    while r < len(best_seller):
        if best_seller[r] == best_seller[l]:
            streak += 1
            if streak == k:
                return True
        else:
            streak = 1
            l = r
        r += 1
    return False

# same idea, deriving the run length from the pointers instead of a separate counter
def best_seller_streak(best_seller, k):
    l, r = 0, 0
    while r < len(best_seller):
        if best_seller[r] == best_seller[l]:
            r += 1
            if r - l == k:
                return True
        else:
            l = r
    return False

# same fixed-window skeleton as P38.3, but the win condition flips: all k days the SAME window full (r - l == k): len(freq_map) == 1 → one distinct title → True, else False
#
# n: number of days
# k: window width
# T: O(n) — each day enters and leaves the window once
# S: O(k) — freq_map holds at most k titles

from collections import defaultdict


def best_seller_streak(best_seller, k):
    l, r = 0, 0
    freq_map = defaultdict(int)
    while r < len(best_seller):
        freq_map[best_seller[r]] += 1
        r += 1
        if r - l == k:
            if len(freq_map) == 1:
                return True
            freq_map[best_seller[l]] -= 1
            if freq_map[best_seller[l]] == 0:
                del freq_map[best_seller[l]] 
            l += 1
    return False


# # Enduring Best Seller Streak

# We are given an array, `best_seller`, with the title of the most sold book for each day over a given period. We are also given a number `k` with `1 ≤ k ≤ len(sales)`.

# We need to return whether there is any k-day period where every day has the **same** best-selling title.

# Example 1:
# best_seller = ["book3", "book1", "book3", "book3", "book2"]
# k = 3

# Output: False
# No three consecutive days have the same best seller.

# Example 2:
# best_seller = ["book3", "book1", "book3", "book3", "book2"]
# k = 2

# Output: True
# Days 3-4 have the same best seller "book3".

# Example 3:
# best_seller = ["book1", "book2", "book1"]
# k = 2

# Output: False
# No two consecutive days have the same best seller.

# Example 4:
# best_seller = ["book1", "book1", "book1"]
# k = 3

# Output: True
# The entire array has the same best seller.

# Constraints:

# - The length of `best_seller` is at most `10^6`
# - Each book title has length at most `100`
# - `1 <= k <= len(best_seller)`