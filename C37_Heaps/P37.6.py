# k-way merge across the already-sorted genre lists
#   seed the heap with the front (most-played) song of every genre:
#     (-plays, title, genre idx, song idx)
#   heapify the seed in O(m)  (an equivalent push-loop would be O(m log m))
#   pop k times — each pop yields the next most-listened title:
#     record the title
#     push the next song from that same genre (if any)
#
# m: number of genres   
# k: songs to return
# T: O(m + k * log m) - heapify seed O(m) + k pop/push rounds, each heap op O(log m)
# S: O(m + k) - heap holds up to m entries (one per genre), res holds k titles

import heapq


def most_listened(genres, k):
    # seed with heapify: O(m)
    heap = [(-genre[0][1], genre[0][0], i, 0) for i, genre in enumerate(genres)]
    heapq.heapify(heap)
    # equivalent but O(m log m) - m pushes, each O(log m):
    # heap = []
    # for i, genre in enumerate(genres):
    #     heapq.heappush(heap, (-genre[0][1], genre[0][0], i, 0))  # -plays, title, genre idx, song idx

    res = []
    while len(res) < k:
        _, title, i, pos = heapq.heappop(heap)
        res.append(title)
        if pos + 1 < len(genres[i]):
            nxt = genres[i][pos + 1]
            heapq.heappush(heap, (-nxt[1], nxt[0], i, pos + 1))

    return res


# # Most Listened Across Genres

# You are given an array, `genres`, of length `m`, where each element is an array of songs from a given genre. Each song consists of a `[title, plays]` pair.

# - Each list is non-empty and **already sorted** from most to least played songs.
# - There are `n > 0` songs in total, and each song appears in at most one list.

# You are also given a positive integer `k` satisfying `1 <= k <= n`. Return the titles of the top `k` most-listened songs across all genres, in order from most to least listened. It doesn't matter how you break ties.

# Example:
# genres = [
#   [ # Pop
#     ["Coding In The Deep", 123],
#     ["Someone Like GNU",    99],
#     ["Hello World",         98]
#   ],
#   [ # Country
#     ["Ring Of Firewalls",  217]
#   ],
#   [ # Rock
#     ["Boolean Rhapsody",   184],
#     ["Merge Together",     119],
#     ["Hey Queue",          102]
#   ]
# ]
# k = 5
# Output: [
#   "Ring Of Firewalls",
#   "Boolean Rhapsody",
#   "Coding In The Deep",
#   "Merge Together",
#   "Hey Queue"
# ]

# Constraints:

# - The length of `genres`, `m`, is at least `1` and at most `10^5`.
# - The total number of songs, `n`, is at least `1` and at most `10^5`.
# - Song titles are unique and have at most `50` characters.
# - Each genre list is already sorted from most to least played songs (there can be ties).
# - `1 <= k <= n`.