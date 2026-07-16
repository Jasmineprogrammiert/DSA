# # Pattern — Difference Array (many range updates, read at the end)   [NEW]
#
# Trigger: many "add v to every [l, r]" updates, answer needed only at the end
#     -> naive rewrites the whole range each time = O(n * updates) -> TLE
#
# Idea: running never resets, so ONE write spreads rightward forever.
# Post each update twice: the vote at l, its canceller at r+1.
#
#     e.g. [l=1, r=3, +v] on n=6:      minute:  0   1   2   3   4   5
#     diff[l]   += v   ->  on forever           .  +v  +v  +v  +v  +v
#     diff[r+1] -= v   ->  off forever          .   .   .   .  -v  -v
#                                              ------------------------
#     net after sweep                           .  +v  +v  +v   .   .   = [l, r]
#
# Sweep: running IS the live answer — the net count at the minute you stand on.
#     Neighbor minutes differ only by what starts/stops at the boundary, and
#     diff[i] is exactly that change:
#         count(i) = count(i-1) + diff[i]   ->   running += diff[i]; out[i] = running
#
# Gotchas:
#     - both notes sit on the FIRST minute of their new state (in: l, out: r+1)
#     - size diff n+1 so a range ending at n-1 has a cell for its canceller
#
# diff = [0] * (n + 1)
# for l, r, v in votes:
#     ...                 -> +v at l, -v at r+1
# out = [0] * n; running = 0
# for i in range(n):
#     ...                 -> running += diff[i]; out[i] = running
#
# n: length of the video in minutes
# u: number of votes
# T: O(n + u) — 2 writes per vote, then one sweep; range width never matters
# S: O(n) — the diff array (n + 1 cells) and the output

def net_votes(n, votes):
    diff = [0] * (n + 1)
    for l, r, v in votes:
        diff[l] += v  # +v forever from l (the sweep's carry spreads it)
        diff[r + 1] -= v  # canceller: -v forever from r+1 -> net +v on [l, r]
    out = [0] * n
    running = 0
    for i in range(n):
        running += diff[i]  # apply this minute's change -> count at i
        out[i] = running
    return out


# # Segmented Video Votes

# YouTube is testing an experimental API that allows users to like or dislike specific segments of a video instead of the entire video. You are provided with:

# `n`: the length of the video in minutes.

# `votes`: an array where each element represents a user's vote and is structured as an array with 3 integers:

# - `l`: the starting minute of the vote (inclusive)
# - `r`: the ending minute of the vote (inclusive)
# - `v`: the vote value (1 for like, -1 for dislike)

# Each vote satisfies `0 ≤ l ≤ r < n`. The votes can be in any order and may overlap.
# Your task is to return an array of length `n`, where each index `i` contains the _net vote count_ at minute `i`.

# Example:
# n = 6
# votes = [
#   [3, 4, 1],
#   [0, 0, 1],
#   [1, 3, 1],
#   [0, 5, -1]
# ]

# Output: [0, 0, 0, 1, 0, -1]
# The net vote counts after applying each vote are:

# - [0, 0, 0, 1, 1, 0]
# - [1, 0, 0, 1, 1, 0]
# - [1, 1, 1, 2, 1, 0]
# - [0, 0, 0, 1, 0, -1]

# Constraints:

# - `1 <= n <= 10^5`
# - `0 <= votes.length <= 10^5`
# - `votes[i].length` is `3`
# - `0 <= votes[i][0] <= votes[i][1] < n`
# - `votes[i][2]` is either `1` or `-1`