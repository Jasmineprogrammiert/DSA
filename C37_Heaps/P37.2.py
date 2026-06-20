# "Largest k" by plays, output order free, follow-up wants O(k) space.
#   Max-heap: heapify all, pop k times   T: O(n + k log n)  S: O(n)
#   Min-heap, size k:                    T: O(n log k)      S: O(k)
#       for each (plays, title):
#           heap under k -> push
#           else beats root -> heapreplace   # pop-then-push, one sift
#       return the titles left
# n: number of songs
# T: O(n log k) — one O(log k) heap op per song, n songs in total
# S: O(k) — the heap holds at most k songs

import heapq


def k_most_played(songs, k):
    min_heap = []
    for title, plays in songs:
        if len(min_heap) < k:
            heapq.heappush(min_heap, (plays, title))
        elif plays > min_heap[0][0]:
            heapq.heapreplace(min_heap, (plays, title))
    return [title for _, title in min_heap]


# # K Most Played

# You are given a list of `(title, plays)` tuples where the first element is the name of a song, and the second is the number of times the song has been played. You are also given a positive integer `k`. Return the `k` most played songs from the list, in any order.

# - If the list has fewer than `k` songs, return all of them.
# - Break ties in any way you want.
# - You can assume that song titles have a length of at most `50`.

# Example:
# songs = [["All the Single Brackets", 132],
#          ["Oops! I Broke Prod Again", 274],
#          ["Coding In The Deep", 146],
#          ["Boolean Rhapsody", 193],
#          ["Here Comes The Bug", 291],
#          ["All About That Base Case", 291]]
# k = 3
# Output: ["All About That Base Case", "Here Comes The Bug", "Oops! I Broke Prod Again"]. Any order of these (excellent) songs would be valid.

# Follow-up: Can you solve it using only `O(k)` space?

# Constraints:

# - The length of `songs` is at most `10^5`
# - Each element in `songs` is a tuple with a string and an integer
# - All song titles are unique
# - The length of the string in each song is at most `50`
# - `1 <= k <= 10^5`