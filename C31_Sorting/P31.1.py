# Use a frequency map to count the appearance of the letter, Map<letter, count>
# Sort the letters by count descending
# If two frequencies are the same, break the tie alphabetically
# Return the sorted list of letters
# 
# n: length of word
# T: O(n) - iterate through each char to build frequency map, sorting is O(1) since at most 26 letters
# S: O(1) - frequency map and result list are bounded by 26 lowercase letters

def sorting_by_frequency(word):
    count = dict()
    for char in word:
        if char not in count:
            count[char] = 0
        count[char] += 1
    
    return sorted(count, key=lambda char: (-count[char], char))

# print(sorting_by_frequency("supercalifragilisticexpialidocious"))



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