# is_stolen = lambda t: t >= 3 
# is equal to
# def is_stolen(t):
#     return t >= 3
# https://www.w3schools.com/python/python_lambda.asp

# Use the middle point between l and r to crack down the range
# Can either shrink down l and r step by step till they're adjacent, or
# check of m is at the adjacent point of l and r
# All the timestamps before l are false, after r are true
# The binary search is stopped when l = r, where the value first becomes True
# n = t2 - t1
# T: O(log n) - the number of steps is roughly how many times n can be divided by 2 till it gets down to 1
# S: O(1)
# both methods work, which one to use depends on your preference

def find_first_stolen(t1, t2, is_stolen):
    def is_before(t):
        return not is_stolen(t)
    
    l, r = t1, t2
    while r - l > 1: # stops when r and l are adjacent
        m = (l + r) // 2
        if is_before(m):
            l = m
        else:
            r = m
    return r # by the loop's end, l points to the last timestamp where the bike was not stolen, so r points to the first timestamp where the bike is stolen

# def find_first_stolen(t1, t2, is_stolen):
#     l, r = t1, t2
    
#     while l < r:
#         m = (l + r) // 2
#         if is_stolen(m):
#             r = m
#         else:
#             l = m + 1
#     return l



# # CCTV Footage

# You are given an API called `is_stolen(t)` which takes a timestamp as input and returns `True` if the bike is missing at that timestamp and `False` if it is still there. You're also given two timestamps, `t1` and `t2`, representing when you parked the bike and when you found it missing. Return the timestamp when the bike was first missing, minimizing the number of API calls. Assume that `0 < t1 < t2`, `is_stolen(t1)` is `False`, and `is_stolen(t2)` is `True`.

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/binary-search-fig2.png

# Example 1: t1 = 1, t2 = 5, is_stolen = lambda t: t >= 3
# Output: 3. The bike was stolen at timestamp 3.

# Example 2: t1 = 1, t2 = 10, is_stolen = lambda t: t >= 7
# Output: 7. The bike was stolen at timestamp 7.

# Example 3: t1 = 5, t2 = 10, is_stolen = lambda t: t >= 8  
# Output: 8. The bike was stolen at timestamp 8.

# Constraints:

# - `0 < t1 < t2 ≤ 10^6`
# - The API call `is_stolen(t)` takes `O(1)` time