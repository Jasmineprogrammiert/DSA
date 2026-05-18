# Problem 37.4 - Top Songs Class With Updates
# Same as 37.3 but register_plays can be called with the same title multiple
# times; new plays are added to the total.
#
# Example:
# s = TopSongs(3)
# s.register_plays("Boolean Rhapsody", 100)
# s.register_plays("Boolean Rhapsody", 193)  # Total 293
# s.register_plays("Coding In The Deep", 75)
# s.register_plays("Coding In The Deep", 75)  # Total 150
# s.register_plays("All About That Base Case", 200)
# s.register_plays("All About That Base Case", 90)  # Total 290
# s.register_plays("All About That Base Case", 1)   # Total 291
# s.register_plays("Here Comes The Bug", 223)
# s.register_plays("Oops! I Broke Prod Again", 274)
# s.register_plays("All the Single Brackets", 132)
# s.top_k()  # ["All About That Base Case","Boolean Rhapsody","Oops!..."]
#
# Constraints:
# - 0 < k < 1000
# - Song titles unique, length <= 50
# - Each register call plays >= 1, total never exceeds 10^9