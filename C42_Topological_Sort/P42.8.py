# Problem 42.8 - Number of Palindromic Splits
# A palindromic split of a string is a way of dividing a string into
# substrings where every substring is a palindrome.
# Given a string s, return the number of palindromic splits.
#
# Example 1: s = "abbaab" -> 6
# a|b|b|a|a|b, a|bb|a|a|b, a|b|b|aa|b, a|bb|aa|b, abba|a|b, a|b|baab
#
# Example 2: s = "aabaa" -> 6
# a|a|b|a|a, aa|b|a|a, a|a|b|aa, aa|b|aa, a|aba|a, aabaa
#
# Example 3: s = "aaaaa" -> 16
#
# Example 4: s = "" -> 0
#
# Constraints:
# - len(s) <= 10^4
# - Each character is a lowercase English letter