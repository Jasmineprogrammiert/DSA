# return a sorted array with all the letters from
#       most frequent to least frequent
#       break the tie alphabetically

# sorted(freq_map) based on count, then alphabetically if tie
# list(keys in sorted freq_map)

# n: length of word
# T: O(n) - each letter in word is iterated once; the sort is over at most 26 keys, O(26 log 26) = O(1)
# S: O(1) - regardless of the length of word, the dictionary and the result hold at most 26 letters

from collections import defaultdict

def sorting_by_frequency(word):
    freq_map = defaultdict(int)
    for w in word:
        freq_map[w] += 1
    
    return sorted(freq_map, key=lambda ch: (-freq_map[ch], ch))


# # Sorting By Frequency

# Given a string, `word`, consisting of lowercase letters only, return a sorted array with all the letters in `word` sorted from most frequent to least frequent. If two frequencies are the same, break the tie alphabetically.

# Example 1: word = "supercalifragilisticexpialidocious"
# Output: ['i', 'a', 'c', 'l', 's', 'e', 'o', 'p', 'r', 'u', 'd', 'f', 'g', 't', 'x']

# Example 2: word = "aabbbcccc"
# Output: ['c', 'b', 'a']. 'c' appears 4 times, 'b' appears 3 times, and 'a' appears 2 times.

# Example 3: word = "abc"
# Output: ['a', 'b', 'c']. All letters appear once, so they are sorted alphabetically.

# Constraints:

# - The length of `word` is at most `10^5`
# - `word` contains only lowercase letters