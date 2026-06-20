# Data Structures:
#       dict title->plays (lookup)
#       lower = max-heap, upper = min-heap (median)
# Invariants:
#       max(lower) <= min(upper)
#       len(lower) == len(upper) [+1 odd extra in lower]
#
# register_plays(title, plays):
#     plays[title] = plays
#     push plays -> lower
#     move lower's max -> upper        # keep ordering
#     if len(upper) > len(lower):
#         move upper's min -> lower    # keep sizes
#
# is_popular(title):
#     median = avg(lower top, upper top) if equal size else lower top
#     return plays[title] > median
#
# Median sits at the boundary between the two halves:
#    lower half          |          upper half
#    132   140   193     |     223   274   291
#                 ^             ^
#             -lower[0]      upper[0]
#         (largest of low)   (smallest of up)

# n: number of registered songs
# T: register O(log n), is_popular O(1) - heap push/pop is log n; median is two heap-top reads
# S: O(n) - dict + two heaps each hold all n songs

import heapq


class PopularSongs:
    def __init__(self):
        self.plays = {}
        self.lower = []  # max-heap (values negated): smaller half
        self.upper = []  # min-heap: larger half

    def register_plays(self, title, plays):
        self.plays[title] = plays
        heapq.heappush(self.lower, -plays)
        heapq.heappush(self.upper, -heapq.heappop(self.lower))
        if len(self.upper) > len(self.lower):
            heapq.heappush(self.lower, -heapq.heappop(self.upper))

    def is_popular(self, title):
        if len(self.lower) == len(self.upper):
            median = (-self.lower[0] + self.upper[0]) / 2
        else:
            median = -self.lower[0]
        return self.plays[title] > median


# # Popular Songs Class

# Implement a `PopularSongs` class that has two methods:

# - `register_plays(title, plays)` indicates that a song was played a given number of times. It returns nothing. The method is never called with the same title twice.
# - `is_popular(title)` returns whether the given song is popular. A song is _popular_ if its play count is strictly higher than the median play count.

# The median of a collection of integers with odd size is the middle element in sorted order; if the size is even, the median is the average of the two middle elements.

# Example:

# p = PopularSongs()
# p.register_plays("Boolean Rhapsody", 193)
# p.is_popular("Boolean Rhapsody")                   # Returns False
# p.register_plays("Coding In The Deep", 140)
# p.register_plays("All the Single Brackets", 132)
# p.is_popular("Boolean Rhapsody")                   # Returns True
# p.is_popular("Coding In The Deep")                 # Returns False
# p.is_popular("All the Single Brackets")            # Returns False
# p.register_plays("All About That Base Case", 291)
# p.register_plays("Oops! I Broke Prod Again", 274)
# p.register_plays("Here Comes The Bug", 223)
# p.is_popular("Boolean Rhapsody")                   # Returns False
# p.is_popular("Here Comes The Bug")                 # Returns True

# Analyze the space and runtime of each operation in terms of the number of songs registered so far. The goal is to minimize the total runtime assuming we will make the same number of operations of each type.

# Constraints:

# - Song titles are unique and have at most `50` characters.
# - The number of plays is at least `1` and at most `10^9`.
# - The number of registered songs is at most `10^5`.
