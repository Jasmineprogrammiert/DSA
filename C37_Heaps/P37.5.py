# dict = { title: plays }
# lower = [] <-- max-heap via negative counts; equal size to upper or one extra
# upper = [] <-- min-heap via positive counts
# median

# n: number of registered songs
# T: O(log n) per registration/query pair - register_plays is O(log n); is_popular is O(1) average
# S: O(n) - dictionary stores n songs; the two heaps together store n counts

import heapq

class PopularSongs:
    def __init__(self):
        self.plays = {}
        self.lower = []
        self.upper = []

    def register_plays(self, title, plays):
        self.plays[title] = plays
        if not self.lower or plays <= -self.lower[0]:
            heapq.heappush(self.lower, -plays)
        else:
            heapq.heappush(self.upper, plays)

        if len(self.lower) > len(self.upper) + 1:
            heapq.heappush(self.upper, -heapq.heappop(self.lower))
        elif len(self.upper) > len(self.lower):
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