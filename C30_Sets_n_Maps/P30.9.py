# Compute each word's alphabetical sum -> ord(char) - ord('a') + 1, store sums in a set
# Reuse is allowed, so only presence matters, not frequency (use a set, not a map)
# Key insight: words have at most 3 letters worth at most 26 each, so sums range 1-78 -> at most 78 distinct values regardless of input size
# Two loops over the set: fix a and b, then c = target / (a * b) is forced
# Check target % (a * b) == 0 first (c must be a positive integer), then look up c in the set

# n: number of words
# T: O(n) - one pass to build the set O(n), nested loop over at most 78 * 78 values O(1)
# S: O(1) - set holds at most 78 values regardless of input size

def product_of_alphabetical_sum(words, target):
    values = set()
    
    def alphabetical_sum(word):
        val = 0
        for char in word:
            val += ord(char) - ord('a') + 1
        return val
    
    for word in words:
        values.add(alphabetical_sum(word))

    for i in values:
        if target % i != 0:
            continue
        for j in values:
            k = target / (i * j)
            if k in values:
                return True
    return False

# def product_of_alphabetical_sum(words, target):
#     values = set()
    
#     for word in words:
#         val = 0
#         for char in word:
#             val += ord(char) - ord('a') + 1
#         values.add(val)

#     for i in values:
#         for j in values:
#             remainder = target % (i * j)
#             if remainder == 0:
#                 quotient = target // (i * j)
#                 if quotient in values:
#                     return True
#     return False



# # Product of Alphabetical Sums

# Given a list of lowercase strings, `words`, where each string has between `1` and `3` letters, determine if there exist three strings such that the product of their _alphabetical sums_ is a given target value, `target`. The alphabetical sum of a string is the sum of the positions of its letters in the alphabet (e.g., the alphabetical sum of "abz" is `1 + 2 + 26 = 29`). Return true if such a triplet exists. The same string can be used more than once.

# Example 1: words = ["abc", "fg", "hij", "klm", "nop", "qrs", "vwx"], target = 1620
# Output: true
# Explanation: The triplet is "abc", "abc", "nop": 6 * 6 * 45 = 1620.

# Example 2: words = ["a", "b"], target = 2
# Output: true
# Explanation: The triplet is "a", "a", "b": 1 * 1 * 2 = 2.

# Example 3: words = ["a", "b", "c"], target = 7
# Output: false
# Explanation: No triplet of strings has a product of alphabetical sums equal to 7.

# Constraints:

# - `0 ≤ words.length ≤ 10^5`
# - Each string in `words` has length between `1` and `3`
# - All strings contain only lowercase English letters
# - `1 ≤ target ≤ 10^6`