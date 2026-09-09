# n: length of s
# k: length of s2, k = n + 1
# T: O(n) - init is one pass over s; each method call is O(1) to copy the map plus one pass over s2
# S: O(1) - keys are lowercase letters, so the map holds at most 26 entries however long s is

# length check, then count s once and spend the counts against s2 - more than one extra fails

from collections import defaultdict

class Checker:
    def __init__(self, s):
        self.s = s
        self.freq_count = defaultdict(int)
        for char in s:
            self.freq_count[char] += 1
    
    def expands_into(self, s2):
        if len(self.s) + 1 != len(s2):
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