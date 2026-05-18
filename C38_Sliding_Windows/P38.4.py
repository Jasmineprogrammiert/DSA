# Problem 38.4 - Enduring Best Seller Streak
# Given an array best_seller and a number k, return whether there is any
# k-day period where every day has the same best-selling title.
#
# Example 1: ["book3","book1","book3","book3","book2"], k = 3 -> False
# Example 2: ["book3","book1","book3","book3","book2"], k = 2 -> True
# Example 3: ["book1","book2","book1"], k = 2 -> False
# Example 4: ["book1","book1","book1"], k = 3 -> True
#
# Constraints:
# - len(best_seller) <= 10^6
# - 1 <= k <= len(best_seller)