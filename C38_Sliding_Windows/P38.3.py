# set           the window must be ALL-DISTINCT - every count is 1
# freq map      counts matter: l evicts blind (fixed-length), or duplicates are allowed
#
# fixed-length      movement is unconditional. r every pass, l every full window.
#                   the data affects only the CHECK, never the pointers
# max/min           movement is data-driven. l moves only while the window is invalid
#                   so how far it moves depends on what's in it


# ---- 1. fixed-length window + freq map ----

# freq_map counts the titles in [l, r); len(freq_map) is the distinct count
#
# INIT l = r = 0, freq_map = defaultdict(int)
# while r < len(best_seller):
#     freq_map[best_seller[r]] += 1
#     r += 1
#     when r - l == k
#         len(freq_map) == k:
#             return True
#         freq_map[best_seller[l]] -= 1, del 0
#         l += 1
#         to keep the window at length k
# return False

# n: number of days
# k: window width
# T: O(n) — each day enters and leaves the window once
# S: O(k) — freq_map holds at most k titles

# k = 3
# 0 1 2 3 4 5 6 7       INDEX
# 3 1 3 3 2 3 4 3       BOOK_SELLER
#         l  
#               r
# freq_map = {2: 1, 3: 1, 4: 1}

from collections import defaultdict

def unique_best_seller(best_seller, k):
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


# ---- 2. maximum window + set ----

# seen holds exactly the titles in [l, r), all distinct
#
# INIT l = r = 0, seen = set(), cur_best = 0
# while r < len(arr):
#     while arr[r] in seen:
#         remove arr[l]
#         l += 1
#     seen.add(arr[r])
#     r += 1
#     cur_best = max(cur_best, r - l)
#     if cur_best == k:
#         return True
# return False

# n: length of best_seller
# k: length of the window
# T: O(n) - r advances n times; l only moves forward, at most n times total
# S: O(k) - seen never exceeds the window, and the window never exceeds k

# k = 3
# 0 1 2 3 4 5 6 7       INDEX
# 3 1 3 3 2 3 4 3       BOOK_SELLER
#         l  
#               r
# seen = {2, 3, 4}
# cur_best = 3

def unique_best_seller_set(best_seller, k):
    l, r = 0, 0
    seen = set()
    cur_best = 0

    while r < len(best_seller):
        while best_seller[r] in seen:
            seen.remove(best_seller[l])
            l += 1

        seen.add(best_seller[r])
        r += 1

        cur_best = max(cur_best, r - l)
        if cur_best == k:
            return True
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