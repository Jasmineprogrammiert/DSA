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