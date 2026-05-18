# Problem 37.3 - Top Songs Class
# Implement a TopSongs class with:
# - __init__(k): k > 0
# - register_plays(title, plays): registers a song. Never called with same title twice.
# - top_k(): returns the (up to) k titles with most plays, any order, ties arbitrary.
#
# Example:
# s = TopSongs(3)
# s.register_plays("Boolean Rhapsody", 193)
# s.register_plays("Coding In The Deep", 146)
# s.top_k()  # ["Coding In The Deep", "Boolean Rhapsody"]
# s.register_plays("All About That Base Case", 291)
# s.register_plays("Here Comes The Bug", 223)
# s.register_plays("Oops! I Broke Prod Again", 274)
# s.register_plays("All the Single Brackets", 132)
# s.top_k()  # ["All About That Base Case","Here Comes The Bug","Oops!..."]
#
# Constraints:
# - 0 < k < 1000
# - Song titles unique, length <= 50
# - Plays >= 1 and <= 10^9