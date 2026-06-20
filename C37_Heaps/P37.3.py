# Goal: track the up-to-k most-played songs, minimize total runtime
#   Brute force: store all, sort on read -> register O(1), top_k O(n log n)
#   Optimized:   min-heap capped at k, drop any plays <= heap[0]
#                -> register O(log k), top_k O(k)

# n: songs registered so far
# k: heap cap (k << n)
# register_plays T: O(log k) - one push/replace on a heap capped at k
# top_k T: O(k) - walk the <= k heap entries into a list
# S: O(k) - heap holds at most k songs; no recursion -> O(1) call stack

import heapq


class TopSongs:
    def __init__(self, k):
        self.k = k
        self.min_heap = []

    def register_plays(self, title, plays):
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, (plays, title))
        elif plays > self.min_heap[0][0]:
            heapq.heapreplace(self.min_heap, (plays, title))

    def top_k(self):
        return [title for _, title in self.min_heap]


# # Top Songs Class

# Implement a `TopSongs` class that receives an integer `k > 0` during initialization and has two methods:

# - `register_plays(title, plays)` indicates that a song was played a given number of times. It returns nothing. The method is never called with the same title twice.
# - `top_k()` returns the (up to) `k` registered song titles with the most plays, in any order, and breaking ties arbitrarily.

# Example:
# s = TopSongs(3)
# s.register_plays("Boolean Rhapsody", 193)
# s.register_plays("Coding In The Deep", 146)
# s.top_k()  # Returns ["Coding In The Deep", "Boolean Rhapsody"]
# s.register_plays("All About That Base Case", 291)
# s.register_plays("Here Comes The Bug", 223)
# s.register_plays("Oops! I Broke Prod Again", 274)
# s.register_plays("All the Single Brackets", 132)
# s.top_k()  # Returns ["All About That Base Case", "Here Comes The Bug", "Oops! I Broke Prod Again"]

# Analyze the space and runtime of each operation in terms of the number of songs registered so far. The goal is to minimize the total runtime assuming we will make the same number of operations of each type and that `k` will be relatively small compared to the number of songs.

# Constraints:

# - `0 < k < 1000`.
# - Song titles are unique and have at most `50` characters.
# - The number of plays is at least `1` and at most `10^9`.
# - Song titles are unique and have at most `50` characters.
