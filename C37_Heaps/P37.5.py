# Problem 37.5 - Popular Songs Class
# Implement a PopularSongs class:
# - register_plays(title, plays): registers a song (never same title twice)
# - is_popular(title): returns whether the song's play count is strictly
#   higher than the median play count
# Median: middle element (odd), average of two middle (even).
#
# Example:
# p = PopularSongs()
# p.register_plays("Boolean Rhapsody", 193)
# p.is_popular("Boolean Rhapsody")            # False
# p.register_plays("Coding In The Deep", 140)
# p.register_plays("All the Single Brackets", 132)
# p.is_popular("Boolean Rhapsody")            # True
# p.is_popular("Coding In The Deep")          # False
# p.register_plays("All About That Base Case", 291)
# p.register_plays("Oops! I Broke Prod Again", 274)
# p.register_plays("Here Comes The Bug", 223)
# p.is_popular("Boolean Rhapsody")            # False
# p.is_popular("Here Comes The Bug")          # True
#
# Constraints:
# - Song titles unique, length <= 50
# - Plays >= 1 and <= 10^9
# - Up to 10^5 registered songs