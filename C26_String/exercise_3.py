# def index_of(s, t):
#     if not t:
#         return 0
#     if not s:
#         return -1

#     for i in range(len(s) - len(t) + 1):
#         if s[i : i + len(t)] == t:
#             return i
#     return -1
  
def index_of(s, t):
    if not t:
        return 0
    if not s:
        return -1

    for i in range(len(s) - len(t) + 1):
        for j in range(len(t)):
            if s[i + j] != t[j]:
                break
        else:
            return i
    return -1

# T: O(len(s) * len(t))
    # The outer loop runs O(len(s)) times, and the inner loop runs O(len(t)) times in the worst case
# S: O(1)
    # comparing characters like s[i + j] != t[j] access existing strings without creating any new data structures or storing additional information
    # The variables i and j are just loop counters that take constant space regardless of input size.



# # String Matching

# Implement an `index_of(s, t)` method, which returns the first index where string `t` appears in string `s`, or -1 if `s` does not contain `t`.

# Example 1: s = "hello world", t = "world"
# Output: 6

# Example 2: s = "needle in a haystack", t = "needle"
# Output: 0

# Example 3: s = "needle in a haystack", t = "not"
# Output: -1

# Constraints:

# - The input strings can contain any valid ASCII character
# - The length of s is at most 10^5
# - The length of t is at most 10^5
# - t can be empty, in which case return 0
# - s can be empty, in which case return -1 if t is non-empty, 0 if t is empty