# char not in `brackets` do not affect whether `s` is balanced
# cannot surround only half of a matching pair of another type of brackets
# `brackets` does not contain any repeated characters

# opening = {       SET()
#   (,
#   [,
#   {
# }
# closing = {       DICT()
#   ): (,
#   ]: [,
#   }: {
# }

# stack = [
#    ( )
# ]
# s = "((a+b)*[c-d]-{e/f})"

# n: length of s
# k: length of brackets (k <= 10, so O(1))
# T: O(n) - one pass over s, O(1) per char; building the set and dict is O(k)
# S: O(n) - the stack holds every open seen so far, all of s in the worst case; set and dict are O(k)

def custom_brackets(s, brackets):
    opening = set()
    closing = dict()
    for b in brackets:
        opening.add(b[0])
        closing[b[1]] = b[0]

    stack = []
    for elem in s:
        if elem in opening:
            stack.append(elem)
        elif elem in closing:
            if not stack or stack[-1] != closing[elem]:
                return False
            else:
                stack.pop()
    return not stack


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