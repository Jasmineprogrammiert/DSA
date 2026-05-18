# Problem 42.7 - Supersequence
# A supersequence of a string s is another string that contains all the same
# letters of s in the same relative order. For instance, "aabbcc" is a
# supersequence of "abc", but not of "bca".
#
# Given a non-empty array of strings, arr, where each string consists only
# of lowercase English letters, determine if it is possible to construct a
# single supersequence of all the strings in arr such that no letter appears
# more than once. Return true if such a supersequence exists, false otherwise.
#
# Example 1: arr = ["abc", "bde", "df", "cfe"] -> True
# "abcdfe" is a supersequence.
#
# Example 2: arr = ["ab", "ba"] -> False
# Any supersequence would need 'a' or 'b' twice.
#
# Example 3: arr = ["aa"] -> False
#
# Constraints:
# - Length of each string <= 100
# - Each string consists of lowercase English letters
