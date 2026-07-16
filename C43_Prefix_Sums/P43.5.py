# # Pattern — Sort + Prefix Sums for the sum of |differences|
#
# Trigger:
#     the answer sums ABSOLUTE differences between pairs of values
#     -> abs() is the enemy; sort so every difference has a known sign.
#
# After sorting a[0..m-1], element a[i] is a water line: every left value
# <= it, every right value >= it, so each side's gaps bulk into one
# sign-free chunk that prefix sums give in O(1):
#     left  = i * a[i]                - (a[0] + ... + a[i-1])       me x count - their sum
#     right = (a[i+1] + ... + a[m-1]) - (m - 1 - i) * a[i]          their sum - me x count
#
# Steps: derive the value array -> sort -> prefix sums -> per-element contribution.
#
# n: length of likes / dislikes
# T: O(n log n) — the sort dominates; prefix build and sweep are O(n), O(1) per index
# S: O(n) — the scores and prefix_sum arrays

def unusual_days(likes, dislikes):
    scores = [likes[i] - dislikes[i] for i in range(len(likes))]
    scores.sort()
    n = len(scores)

    # sum of left / sum of right in O(1) -> build prefix sums
    prefix_sum = [0] * n
    prefix_sum[0] = scores[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + scores[i]

    max_deviation = 0
    for i in range(n):
        left, right = 0, 0
        if i > 0:
            # i gaps of (me - them) -> me counted i times, their sum subtracted once
            left = i * scores[i] - prefix_sum[i - 1]
        if i < n - 1:
            # (n-1-i) gaps of (them - me) -> their sum, minus me once per gap
            right = (prefix_sum[n - 1] - prefix_sum[i]) - (n - 1 - i) * scores[i]
        max_deviation = max(max_deviation, left + right)
    return max_deviation


# # YouTube Video Unusual Days

# A YouTuber has fetched the number of likes and dislikes of a video each day since its publication, with the goal of finding days with unusually high or low like-to-dislike ratios.

# We are given two arrays, `likes` and `dislikes`, of length `n`, representing the likes and dislikes on each day.

# The _reception score_ of a day is the number of likes minus the number of dislikes. The _deviation_ between two days is the absolute value of the difference in their reception scores. The _total deviation_ of a given day is the sum of the deviations between it and every other day.

# Find the highest _total deviation_ of any day and return it.

# Example:
# likes    = [3, 6, 1]
# dislikes = [0, 1, 9]

# Output: 24
# The reception scores are [3, 5, -8]. The total deviation of each day is:
# day 0: |3 - 5| + |3 - (-8)| = 2 + 11 = 13
# day 1: |5 - 3| + |5 - (-8)| = 2 + 13 = 15
# day 2: |-8 - 3| + |-8 - 5| = 11 + 13 = 24

# Constraints:

# - The length of `likes` and `dislikes` is at most `10^5`
# - Each element in `likes` and `dislikes` is a non-negative integer less than `10^4`