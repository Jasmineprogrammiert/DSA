# 0 1 2 3 4 5 6 7 8 9       IDX

# 6 3 4 8 7 2 6 5 0 1       LIKES
# 6 0 8 0 0 0 1 8 0 2       DISLIKES

# 0 1 0 1 1 1 1 0 0 0       POSITIVES
# 0 1 1 2 3 4 5 5 5 5       PREFIX_SUM

# [[0, 1], [0, 5], [5, 8], [3, 3]]       PERIODS (inclusive)
# Output: [1, 4, 2, 1]

# positive: more likes than dislikes.
# Return the number of positive days during each periods[i].

# n: number of days (length of likes/dislikes)
# m: number of periods
# T: O(n + m) - build positives and prefix sums in O(n); answer m queries in O(1) each
# S: O(n + m) total - O(n) auxiliary for positives and prefix_sum, plus O(m) output

def video_reception(likes, dislikes, periods):
    n = len(likes)
    positives = [0] * n

    for i in range(n):
        if likes[i] > dislikes[i]:
            positives[i] = 1

    prefix_sum = [0] * n
    prefix_sum[0] = positives[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + positives[i]

    res = []
    for l, r in periods:
        if l > 0:
            res.append(prefix_sum[r] - prefix_sum[l - 1])
        else:
            res.append(prefix_sum[r])
    return res


# # YouTube Video Reception

# A YouTuber has fetched the number of likes and dislikes of a video each day since its publication. We say a day is _positive_ if it has more likes than dislikes.

# We are given:

# - Two arrays, `likes` and `dislikes`, of length `n`, representing the likes and dislikes on each day.
# - An array `periods` of length `p`, where each element is a pair `[l, r]` with `0 ≤ l ≤ r < n`. Each pair represents a time period from day `l` to day `r` _inclusive_.

# Return an array, `results`, of length `p`, where `results[i]` is the number of positive days during `period[i]`.

# Example:
# likes    = [6, 3, 4, 8, 7, 2, 6, 5, 0, 1]
# dislikes = [6, 0, 8, 0, 0, 0, 1, 8, 0, 2]
# periods  = [[0, 1], [0, 5], [5, 8], [3, 3]]

# Output: [1, 4, 2, 1]
# For instance, element 0 (for the period [0, 1]) is 1 because
# day 0 doesn't have more likes than dislikes, but day 1 does.

# Constraints:

# - The length of `likes` and `dislikes` is the same and is at most `10^5`
# - Each element in `likes` and `dislikes` is a non-negative integer less than `10^4`
# - The length of `periods` is at most `10^5`
# - `periods[i].length == 2`
# - `0 <= periods[i][0] <= periods[i][1] < n`