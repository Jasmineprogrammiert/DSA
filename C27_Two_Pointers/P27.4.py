# It has two pointers, l and r. l = 0, r = len(s) - 1
# l moves to the right and r moves to the left
# Check s[l].isalpha() and s[r].isalpha(). Increment l by 1 if the former is false, decrement r by 1 if the latter is false
# If s[l].lower() and s[r].lower() are equal. Increment l and decrement r. Otherwise return false
# Exit the loop and return true when l >= r

def palindromic_sentence(s):
    l, r = 0, len(s) - 1
    
    while l < r:
        if not s[l].isalpha():
            l += 1
        elif not s[r].isalpha():
            r -= 1
        else:
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
    return True

# Inward pointers
# n: length of string
# T: O(n)
# S: O(1)



# Given a string `s`, returne whether its letters form a palindrome ignoring punctuation, spaces, and casing.

# Example 1:
# Input: s = "Bob wondered, 'Now, Bob?'"
# Output: true
# Explanation: Considering only letters and ignoring case, we get "bobwonderednowbob" which is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: Considering only letters and ignoring case, we get "raceacar" which is not a palindrome.

# Constraints:

# - 0 ≤ s.length ≤ 10^6
# - s consists of printable ASCII characters