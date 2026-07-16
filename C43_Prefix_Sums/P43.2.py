# # Pattern — Transform, then Prefix Sum (extends P43.1)
# When a range query asks for a COUNT (or a conditional sum), not a raw sum:
# build a derived array whose value at i encodes what you're counting, then run
# the P43.1 range-sum template on THAT array.
#   e.g. mark[i] = 1 if <condition at i> else 0   -> range sum = count of hits
# Ask: what value at index i makes the sum over [l, r] equal the answer?
#
# n: length of likes/dislikes
# p: length of periods
# T: O(n + p) — O(n) to build positive + prefix_sum, O(p) for the queries (O(1) each, p of them)
# S: O(n) — the positive and prefix_sum arrays

def positive_days(likes, dislikes, periods):
    positive = [0] * len(likes)
    for i in range(likes):
        if likes[i] > dislikes[i]:
            positive[i] = 1
    
    prefix_sum = [0] * len(positive)
    prefix_sum[0] = positive[0]
    for i in range(1, len(positive)):
        prefix_sum[i] = prefix_sum[i-1] + positive[i] # = prev sum + cur val
        
    res = []
    for l, r in periods:
        if l == 0:
            res.append(prefix_sum[r])
        else:
            res.append(prefix_sum[r] - prefix_sum[l-1])  # sum[0..r] - sum[0..l-1] = sum[l..r] -> drop the head before l
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