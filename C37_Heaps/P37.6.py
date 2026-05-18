# Problem 37.6 - Most Listened Across Genres
# Given an array of genres, each containing a sorted (most to least played)
# list of [title, plays] songs, and a positive integer k, return the top k
# most-listened songs across all genres, ordered most to least.
#
# Example:
# genres = [
#   [["Coding In The Deep",123],["Someone Like GNU",99],["Hello World",98]],
#   [["Ring Of Firewalls",217]],
#   [["Boolean Rhapsody",184],["Merge Together",119],["Hey Queue",102]]
# ]
# k = 5
# Output: ["Ring Of Firewalls","Boolean Rhapsody","Coding In The Deep",
#          "Merge Together","Hey Queue"]
#
# Constraints:
# - 1 <= m (genres) <= 10^5
# - 1 <= n (total songs) <= 10^5
# - Each genre list sorted descending by plays
# - 1 <= k <= n