# Problem 43.8 - Segmented Video Votes
# YouTube is testing an API where users can like or dislike specific segments
# of a video. Given:
# - n: the length of the video in minutes.
# - votes: an array where each element is [l, r, v] representing a vote from
#   minute l to r inclusive, with v being 1 (like) or -1 (dislike).
# Return an array of length n where each index i contains the net vote count
# at minute i.
#
# Example:
# n = 6
# votes = [[3, 4, 1], [0, 0, 1], [1, 3, 1], [0, 5, -1]]
# Output: [0, 0, 0, 1, 0, -1]
#
# Constraints:
# - 1 <= n <= 10^5
# - 0 <= len(votes) <= 10^5
# - votes[i].length == 3
# - 0 <= votes[i][0] <= votes[i][1] < n
# - votes[i][2] is either 1 or -1
