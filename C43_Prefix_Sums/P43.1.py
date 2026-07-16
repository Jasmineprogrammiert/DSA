# # Initialization
# prefix_sum = [0] * len(arr)
# prefix_sum[0] = arr[0]            # arr is non-empty
# for i in range(1, len(arr)):
#   prefix_sum[i] = prefix_sum[i-1] + arr[i]

# # Query: sum of subarray [l, r]
# if l == 0:
#   return prefix_sum[r]
# return prefix_sum[r] - prefix_sum[l-1]


# Build prefix sums: prefix_sum[i] = total views from day 0 to day i.
#   prefix_sum[i]  =  prefix_sum[i-1]  +  views[i]
#     total to i         total to i-1      this element
#
# For a period [l, r]:
#   prefix_sum[r]  -  prefix_sum[l-1]  =  sum of [l, r]
#     total to r        total to l-1       what we want
# When l == 0 there is nothing before l, so the answer is just prefix_sum[r].
# 
# n: length of views
# p: length of periods
# T: O(n + p) — n to build the prefix array, p for O(1) per query
# S: O(n) — the prefix_sum array (output not counted)

def channel_views(views, periods):
    if not views:  # constraints promise n > 0; guard anyway before views[0]
        return []
    prefix_sum = [0] * len(views)
    prefix_sum[0] = views[0]
    for i in range(1, len(views)):
        prefix_sum[i] = prefix_sum[i-1] + views[i]

    res = []
    for l, r in periods:
        if l == 0:
            res.append(prefix_sum[r])
        else:
            res.append(prefix_sum[r] - prefix_sum[l-1])
    return res


# # Channel Views

# A YouTuber wants to analyze their channel's performance to see if viewer engagement varies during certain times of the year. We are given:

# - An array, `views`, of length `n > 0`, where `views[i]` represents the number of views on day `i`.
# - An array, `periods`, of length `p > 0`, where each element is a pair `[l, r]` with `0 ≤ l ≤ r < n`. Each pair represents a time period from day `l` to day `r` _inclusive_.

# Return an array, `results`, of integers with length `p`, where `result[i]` is the number of views during period `i`.

# Example:
# views = [3, 5, 4, 8, 7, 2, 5, 3, 2, 3]
# periods = [[0, 1], [0, 5], [5, 8], [3, 3]]

# Output: [8, 29, 12, 8]
# For instance, element 0 is 8 because 3 + 5 = 8.

# Constraints:

# - The length of `views` is at most `10^5`
# - `0 <= views[i] < 10^4`
# - The length of `periods` is at most `10^5`
# - `periods[i].length == 2`
# - `0 <= periods[i][0] <= periods[i][1] < n`