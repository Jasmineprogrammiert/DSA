# Given a string and custom bracket pairs, check if all brackets are properly nested and matched. Non-bracket characters are ignored
# 
# Stack - most recently opened bracket must be closed first (LIFO)
# 
# 1. Build a hashmap from brackets: map each closing bracket -> its matching opening bracket
# Also build a set of all opening brackets. This gives O(1) lookup
# 2. Iterate s:
#       open bracket -> push onto stack
#       close bracket -> check stack is not empty AND stack.pop() matches the expected open bracket. If not, return False
#       Otherwise -> skip it
# 3. Return True only if the stack is empty (no unmatched open brackets left)
# 
# 5 Edge cases:
# - closing bracket when stack is empty -> False
# - leftover open brackets at the end -> False
# 
# n: length of s
# k: length of brackets (k <= 10, constant)
# T: O(n) - brackets loop takes O(k), s loop takes O(n), so O(n + k)
# S: O(n) - stack stores at most n open brackets, dict and set each store at most k entries

def custom_brackets(s, brackets):
    close_to_open = dict()
    open_set = set()
    for pair in brackets:
        close_to_open[pair[1]] = pair[0]
        open_set.add(pair[0])
    
    stack = []
    for c in s:
        if c in open_set:
            stack.append(c)
        elif c in close_to_open:
            if not stack or stack[-1] != close_to_open[c]:
                return False
            stack.pop()
    return len(stack) == 0

# print(custom_brackets("((a+b)*[c-d]-{e/f})", ["()", "[]", "{}"]))



# # Custom Brackets

# Given a string, `s`, and an array of strings, `brackets`, where each element consists of two characters, representing matching opening and closing brackets, return whether `s` is balanced according to those brackets:

# - Characters not in `brackets` do not affect whether `s` is balanced.
# - A pair of matching brackets of one type cannot surround only half of a matching pair of another type of brackets.
# - Assume that `brackets` does not contain any repeated characters.

# Example 1: s = "((a+b)*[c-d]-{e/f})", brackets = ["()", "[]", "{}"]
# Output: True

# Example 2: s = "()[}", brackets = ["()", "[]", "{}"]
# Output: False

# Example 3: s = "([)]", brackets = ["()", "[]", "{}"]
# Output: False

# Example 4: s = "<div> hello :) </div>", brackets = ["<>", "()"]
# Output: False

# Example 5: s = ")))(()((", brackets = [")("]
# Output: True

# Constraints:

# - The length of s is at most 10^5
# - The length of brackets is at most 10