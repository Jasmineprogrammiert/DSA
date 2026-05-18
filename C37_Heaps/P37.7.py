# Problem 37.7 - Make Playlist
# Given a list of [song, artist] tuples, reorder so no two songs by the same
# artist are back-to-back. If impossible, return empty list.
#
# Example:
# songs = [["Coding In The Deep","A Dell"],["Hello World","A Dell"],
#          ["Someone Like GNU","A Dell"],["Make You Read My Logs","A Dell"],
#          ["Hey Queue","The Bugs"],["Here Comes the Bug","The Bugs"],
#          ["Merge Together","The Bugs"],["Dirty Data","Michael JSON"],
#          ["Man in the Middle Attack","Michael JSON"],
#          ["Ring Of Firewalls","Johnny Cache"]]
# Output: interleaved so no consecutive same artist
#
# Constraints:
# - n <= 10^5
# - Song and artist names length <= 100