# reframe balance parentheses as plot heights
# the plot starts at 0, 
# goes up for each opening parenthesis, and
# goes down for each closing parenthesis
# The plot for a balanced string creates a valid 'mountain range outline' that:
#   1. never goes below height 0, and
#   2. ends at height 0
# 
# Start a new substring every time the plot goes back to height 0
# 
# n: length of s
# T: O(n) - sinple pass through the string
# S: O(1) - just two variables

def balanced_partition(s):
    height = 0
    res = 0
    for c in s:
        if c == "(":
            height += 1
        else:
            height -= 1
            if height == 0:
                res += 1
    return res



# # Balanced Partition

# Given a balanced parentheses string, `s`, a _balanced partition_ is a partition of `s` into substrings, each of which is itself balanced. Return the maximum possible number of substrings in a balanced partition.

# Example: s = "((()))(()())()(()(()))"
# Output: 4. The balanced partition with the most substrings is "((()))", "(()())", "()", "(()(()))".

# Constraints:

# - The length of s is at most 10^5
# - s consists only of '(' and ')'