# heap: spend the most-loaded artist first, never the same one back-to-back
#
#   count songs per artist -> max-heap keyed on remaining count
#   each round:
#     pop top artist -> append one song -> decrement their count
#     push prev (last round's artist) back in -> their wait is up
#     still has songs? -> they become prev for next round
#   placed fewer than n songs -> impossible -> return []
#
# n: number of songs
# k: number of artists
# T: O(n * log k) - n placements, each a heap pop + push of O(log k)
# S: O(n) - artist_to_titles holds all n titles; heap/res bounded by O(k)/O(n), and k <= n
#
# TODO (revisit): O(n) no-heap alternative - place the most-frequent artist's
#   songs into even indices 0,2,4,... first, then fill the rest. Same artist
#   always lands >=2 apart, so never adjacent. Drops the log k factor.

import heapq
from collections import defaultdict


def make_playlist(songs):
    artist_to_titles = defaultdict(list)
    for title, artist in songs:
        artist_to_titles[artist].append(title)

    heap = [(-len(titles), artist) for artist, titles in artist_to_titles.items()]
    heapq.heapify(heap)

    res = []
    prev = None
    while heap:
        neg_count, artist = heapq.heappop(heap)
        res.append(artist_to_titles[artist].pop())
        neg_count += 1

        if prev is not None:
            heapq.heappush(heap, prev)
        prev = (neg_count, artist) if neg_count < 0 else None

    if len(res) < len(songs):
        return []
    return res


# # Make Playlist

# Imagine your picky friends give you a list of song–artist tuples to create a playlist. Your task is to reorder the songs so that no two songs by the same artist are played back-to-back. If it's not possible, return an empty list.

# Example:
# songs = [["Coding In The Deep", "A Dell"],
#          ["Hello World", "A Dell"],
#          ["Someone Like GNU", "A Dell"],
#          ["Make You Read My Logs", "A Dell"],
#          ["Hey Queue", "The Bugs"],
#          ["Here Comes the Bug", "The Bugs"],
#          ["Merge Together", "The Bugs"],
#          ["Dirty Data", "Michael JSON"],
#          ["Man in the Middle Attack", "Michael JSON"],
#          ["Ring Of Firewalls", "Johnny Cache"]]

# Output: [
#   "Coding In The Deep",         // A Dell
#   "Hey Queue",                  // The Bugs
#   "Hello World",                // A Dell
#   "Dirty Data",                 // Michael JSON
#   "Someone Like GNU",           // A Dell
#   "Here Comes the Bug",         // The Bugs
#   "Make You Read My Logs",      // A Dell
#   "Man in the Middle Attack",   // Michael JSON
#   "Merge Together",             // The Bugs
#   "Ring Of Firewalls"           // Johnny Cache
# ]

# Constraints:

# - The number of songs, `n`, is at most `10^5`.
# - Each element in `songs` is a tuple with two strings.
# - Song and artist names have at most `100` characters.