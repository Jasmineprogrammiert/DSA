# delete the smallest number of characters necessary to make `s` balanced
# return the resulting string
#
# There may be more than one valid answer

# 0 1 2 3 4 5 6 7 8
# ) ) ( ( ) ) ( ( )
#                 p
#     ^ ^ ^ ^   ^ ^     PAIRS

# stack = [0 1 6]  <-- the indices to delete

# n: length of s
# T: O(n) - two passes over s, O(1) per char (stack push / pop, set lookup); the final join is O(n) once
# S: O(n) - stack, set and res each hold at most n entries

def longest_balanced_subsequence(s):
    stack = []
    for idx, elem in enumerate(s):
        if elem == ")" and stack and s[stack[-1]] == "(":
            stack.pop()
        else:
            stack.append(idx)

    res = []
    stack_set = set(stack)
    for idx, elem in enumerate(s):
        if idx not in stack_set:
            res.append(elem)
    return ''.join(res)


# # Longest Balanced Subsequence

# Given a string of parentheses, `s`, return the longest balanced _subsequence_.

# A subsequence of `s` (not a subarray) is a string obtained by removing some of the letters in `s`. In other words, you have to delete the smallest number of characters necessary to make `s` balanced and return the resulting string. There may be more than one valid answer.

# Example 1: s = "))(())(()"
# Output: "(())()". We removed the following characters:

#    "))(())(()".
#     ^^    ^
# We could have also removed

#    "))(())(()".
#     ^^     ^

# Example 2: s = "(()()"
# Output: "()()". We removed the following character:

#    "(()()"
#     ^
# We could have also removed

#    "(()()"
#        ^

# So "(())" is also a valid output.

# Example 3: s = "())(()"
# Output: "()()". We removed the following characters:

#    "())(()"
#       ^^
# There are several other ways to reach the same answer. For example, we could have also removed

#    "())(()"
#      ^  ^

# Example 4: s = "("
# Output: ""

# Constraints:

# - `0 <= s.length <= 10^5`
# - `s` consists only of `'('` and `')'`