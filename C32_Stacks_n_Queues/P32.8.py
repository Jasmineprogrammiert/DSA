# Stack of indices to track unmatched parentheses
# For each char:
#   If ')' and s[stack top] == '(' -> pop (matched)
#   Otherwise, push index
# Build result by skipping indices left in stack
# 
# n: length of s
# T: O(n) - s iteration happens twice, each time takes O(n)
# S: O(n) - stack or remove has at most n entries

def longest_balanced_subsequence(s):
    stack = []
    for idx, char in enumerate(s):
        if char == ")" and stack and s[stack[-1]] == "(":
            stack.pop()
        else:
            stack.append(idx)
    
    res = []   
    remove = set(stack)
    for idx, char in enumerate(s):
        if idx not in remove:
            res.append(char)
    return ''.join(res)

# print(longest_balanced_subsequence("))(())(()"))



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