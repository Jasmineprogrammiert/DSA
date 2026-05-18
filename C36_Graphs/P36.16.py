# Problem 36.16 - The Floor Is Lava
# Given non-overlapping rectangular furniture pieces [x_min, y_min, x_max, y_max]
# and a max jump distance d, determine if you can reach from the first piece
# (index 0) to the last piece by jumping on furniture.
#
# Example 1:
# furniture = [[1,1,9,5],[12,9,20,13],[16,2,22,7],[24,9,26,11],[29,1,31,5]]
# d = 5 -> True
#
# Example 2: same furniture, d = 4 -> False
#
# Constraints:
# - 1 <= furniture.length <= 1000
# - Pieces are non-overlapping (can share edge/corner)
# - 0 < d <= 10^9