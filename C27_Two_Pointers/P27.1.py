def palindrome(s):
    start = 0
    end = len(s) - 1

    while start < end:
        if s[start] == s[end]:
            start +=1
            end -= 1
        else: 
            return False
    return True

# Algo: Two Pointers (inward)
# n: the length of string
# T: O(n)
# S: O(1)



# # Palindrome Check

# Given a string `s`, return whether `s` is a _palindrome_. A palindrome is a string that reads the same forward and backward.

# Example 1: s = "level"
# Output: true

# Example 2: s = "naan"
# Output: true

# Example 3: s = "hello"
# Output: false

# Constraints:

# - The length of s is at most 10^6
# - s consists of lowercase English letters