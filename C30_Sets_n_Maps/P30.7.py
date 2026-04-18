# Length check - if len(s2) != len(s) + 1, return False upfront
# Build a frequency map of s (since the order doesn't matter)
# Loop through s2, decrementing counts. 
#       If a count goes below 0, either the it isn't in s, or it appears more than the frequency count. Increment integer "extra" from 0
#       If extra > 1, return False
# Return True

# n: the length of s
# m: the length of s2
# T: O(n + m) - build map O(n), loop s2 O(m), look up a map takes O(1). Simplify to O(n) since m = n + 1 after length check
# S: O(1) - since freq_count stores lowercase English characters, it's capped at 26

class Checker:
    def __init__(self, s):
        self.s = s
        self.freq_count = {}
        for char in s:
            self.freq_count[char] = self.freq_count.get(char, 0) + 1
    
    def expands_into(self, s2):
        if len(s2) != len(self.s) + 1:
            return False
        
        extra = 0
        freq = self.freq_count.copy()
        
        for char in s2:
            if char in freq:
                freq[char] -= 1
                if freq[char] < 0:
                    extra += 1
            else: 
                extra += 1
                
            if extra > 1:
                return False
        return True



# # Word Expansion Class

# Implement a class, `Checker`, that receives a string `s` upon initialization. The class must support a method, `expands_into(s2)`, which takes another string and checks if `s2` can be formed by adding exactly one letter to `s1` and reordering the letters. All letters in both strings are lowercase alphabetical characters.

# Example 1:
# checker = Checker("tea")
# print(checker.expands_into("tea"))   # returns False
# print(checker.expands_into("team"))  # returns True
# print(checker.expands_into("seam"))  # returns False

# Example 2:
# checker = Checker("on")
# print(checker.expands_into("nooo"))  # returns False
# print(checker.expands_into("not"))   # returns True
# print(checker.expands_into("now"))   # returns True

# Example 3:
# checker = Checker("")
# print(checker.expands_into("a"))     # returns True
# print(checker.expands_into(""))      # returns False
# print(checker.expands_into("ab"))    # returns False

# Constraints:

# - The length of `s` and `s2` is at most `10^5`
# - All characters are lowercase English letters