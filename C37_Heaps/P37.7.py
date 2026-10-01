# TODO (revisit): O(n) no-heap alternative - place the most-frequent artist's
#   songs into even indices 0,2,4,... first, then fill the rest. Same artist
#   always lands >=2 apart, so never adjacent. Drops the log k factor.

# artist_songs = {
#     "artist1": ["song1", "song2"],
#     "artist2": ["song3", "song4", "song5"],
# }
# heap = [(-3, "artist2"), (-2, "artist1")]
# prev = None

# n: number of songs; k: number of distinct artists
# T: O(n log k) - group n songs, seed with k pushes, then up to n heap rounds; O(n) if k <= 1
# S: O(n) - artist_songs stores n titles, res holds up to n titles, heap holds up to k entries

from collections import defaultdict
import heapq

def make_playlist(songs):
    artist_songs = defaultdict(list)
    for title, artist in songs:
        artist_songs[artist].append(title)

    heap = []
    for artist, s in artist_songs.items():
        heapq.heappush(heap, (-len(s), artist))

    prev = None
    res = []
    while heap:
        neg_count, artist = heapq.heappop(heap)
        res.append(artist_songs[artist].pop())
        neg_count += 1

        if prev is not None:
            heapq.heappush(heap, prev)

        if neg_count < 0:
            prev = neg_count, artist
        else:
            prev = None

    if len(res) == len(songs):
        return res
    else:
        return []


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