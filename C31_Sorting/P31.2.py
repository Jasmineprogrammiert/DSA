# Problem 31.2 - Nested Circles
# Given a non-empty array of circles (center (x,y) and radius r),
# determine whether the circles are nested.
# Nested means: one circle completely surrounds all others (without touching),
# and the remaining circles are themselves nested (recursive).
#
# Example: circles = [((5,3),3), ((5,3),2), ((4,4),5)] -> True
#
# Constraints:
# - len(circles) <= 10^4
# - All coordinates and radii are integers between -10^4 and 10^4