# Problem 43.5 - YouTube Video Unusual Days
# Given two arrays likes and dislikes of length n. The reception score of a
# day is likes[i] - dislikes[i]. The deviation between two days is the
# absolute value of the difference in their reception scores. The total
# deviation of a day is the sum of the deviations between it and every
# other day.
# Find the highest total deviation of any day and return it.
#
# Example:
# likes    = [3, 6, 1]
# dislikes = [0, 1, 9]
# Output: 24
# Reception scores are [3, 5, -8]. Total deviations:
# day 0: |3-5| + |3-(-8)| = 2 + 11 = 13
# day 1: |5-3| + |5-(-8)| = 2 + 13 = 15
# day 2: |-8-3| + |-8-5| = 11 + 13 = 24
#
# Constraints:
# - len(likes) == len(dislikes) <= 10^5
# - Each element in likes and dislikes is a non-negative integer < 10^4
