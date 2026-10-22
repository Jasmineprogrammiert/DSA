# n = 6
# votes = [
#   [3, 4, 1],
#   [0, 0, 1],
#   [1, 3, 1],
#   [0, 5, -1]
# ]

# IDX       0  1  2  3  4  5  6
# DIFF      0  0  0  1 -1 -1  1
# RES       0  0  0  1  0 -1
#                         i
# running = -1

# n: video length in minutes
# m: number of votes
# T: O(n + m) - record two changes per vote, then build the result in one pass
# S: O(n) - diff holds n + 1 entries and res holds n; auxiliary space is also O(n)

def seg_video_votes(n, votes):
    diff = [0] * (n + 1)
    for l, r, v in votes:
        diff[l] += v
        diff[r + 1] -= v

    res = [0] * n
    running = 0
    for i in range(n):
        running += diff[i]
        res[i] = running
    return res


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