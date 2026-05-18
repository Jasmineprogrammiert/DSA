# Problem 37.2 - K Most Played
# Given a list of (title, plays) tuples and a positive integer k, return
# the k most played songs in any order. If fewer than k songs, return all.
# Break ties arbitrarily.
#
# Example:
# songs = [["All the Single Brackets", 132],
#          ["Oops! I Broke Prod Again", 274],
#          ["Coding In The Deep", 146],
#          ["Boolean Rhapsody", 193],
#          ["Here Comes The Bug", 291],
#          ["All About That Base Case", 291]]
# k = 3
# Output: ["All About That Base Case","Here Comes The Bug",
#          "Oops! I Broke Prod Again"]
#
# Follow-up: Can you solve it using only O(k) space?
#
# Constraints:
# - len(songs) <= 10^5
# - Song titles unique, length <= 50
# - 1 <= k <= 10^5