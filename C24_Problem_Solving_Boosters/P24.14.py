# answer = 26*k + m,  counts = [0]*26, index = ord(c) - ord('a')
#
# k = min(counts), subtract k from all   -> 26*k   (k = 0 -> skip)
# m = longest run of non-zeros in counts + counts  (doubled for the wrap)
#
# a lap costs one of each letter and earns 26
# once some count is 0 a letter can't be reused, so only 0 / non-0 matters

# n: len(arr)
# T: O(n) — one pass to count, then O(26) work
# S: O(1) — 26 slots, 52 when doubled


# # Longest Alphabet Chain

# Given an array of lowercase letters `arr`, find the length of the longest alphabet chain you can make by reordering the letters. An alphabet chain is a string where each letter is followed by the next letter in the alphabet, like "def". An alphabet chain can wrap around from 'z' to 'a', as in "xyzab".

# Example 1: arr = "acdf"
# Output: 2. The longest chain is "cd".

# Example 2: arr = "aammzz"
# Output: 2. The longest chain is "za".

# Example 3: arr = "mnopqrstuvwxyzxxmnopxxabcdefghijklmnop"
# Output: 30. The longest chain is "mnopqrstuvwxyzabcdefghijklmnop".

# Constraints:

# - `0 <= arr.length <= 10^5`
# - `arr` consists of lowercase English letters only