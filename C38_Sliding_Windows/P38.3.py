# Problem 38.3 - Unique Best Seller Streak
# Given an array best_seller of book titles and a number k, return whether
# there is any k-day period where each day has a different best-selling title.
#
# Example 1:
# best_seller = ["book3","book1","book3","book3","book2","book3","book4","book3"]
# k = 3 -> True (["book2","book3","book4"])
#
# Example 2: same array, k = 4 -> False
# Example 3: ["book1","book2","book3"], k = 3 -> True
#
# Constraints:
# - len(best_seller) <= 10^6
# - 1 <= k <= len(best_seller)