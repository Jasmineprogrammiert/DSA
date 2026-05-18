# Problem 32.8 - Longest Balanced Subsequence
# Given a string of parentheses s, return the longest balanced subsequence.
# A subsequence is obtained by removing some characters. Delete the smallest
# number of characters to make s balanced and return the resulting string.
# There may be more than one valid answer.
#
# Example 1: s = "))(())(()" -> "(())()"
# Example 2: s = "(()()" -> "()()" or "(())"
# Example 3: s = "())(()" -> "()()"
# Example 4: s = "(" -> ""
#
# Constraints:
# - 0 <= len(s) <= 10^5
# - s consists only of '(' and ')'