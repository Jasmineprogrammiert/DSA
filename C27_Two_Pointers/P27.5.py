# It has two pointers, l and r. l = 0, r = len(s) - 1
# l moves to the right and r moves to the left,
# the former represens lowercase, the latter represents the upper
# Check s[l].islower() and s[r].isupper(). Increment l by 1 if the former is false, decrement r by 1 if the latter is false
# If s[l].lower() and s[r].lower() are equal. Increment l and decrement r. Otherwise return false
# Exit the loop and return true when l = len(s) or r = -1

def reverse_case_match(s):
    l, r = 0, len(s) - 1
    
    while l < len(s) and r >= 0:
        if not s[l].islower():
            l += 1
        elif not s[r].isupper():
            r -= 1
        else:
            if s[l] != s[r].lower():
                return False
            l += 1
            r -= 1
    return True

# Inward pointers
# n: length of string
# T: O(n)
# S: O(1)



# # Reverse Case Match

# Given a string, `s`, where half of the letters are lowercase and half uppercase, return whether the word formed by the lowercase letters is the same as the reverse of the word formed by the uppercase letters. Assume that the length, `n`, is even.

# Example 1:
# Input: s = "haDrRAHd"
# Output: true
# Explanation:
# - Lowercase letters: "hard"
# - Uppercase letters: "DRAH"
# - When reversed, "DRAH" becomes "HARD", which matches "hard" ignoring case.

# Example 2:
# Input: s = "haHrARDd"
# Output: false
# Explanation:
# - Lowercase letters: "hard"
# - Uppercase letters: "HARD"
# - When reversed, "HARD" becomes "DRAH", which doesn't match "hard".

# Example 3:
# Input: s = "BbbB"
# Output: true
# Explanation:
# - Lowercase letters: "bb"
# - Uppercase letters: "BB"
# - When reversed, "BB" becomes "BB", which matches "bb" ignoring case.

# Constraints:

# - 0 ≤ s.length ≤ 10^6
# - s contains only uppercase and lowercase English letters