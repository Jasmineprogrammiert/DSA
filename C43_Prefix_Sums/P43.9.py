# Problem 43.9 - Most Booked Slot
# In a mock interview booking system, given:
# - An array slots of length n > 0, where slots[i] is the number of
#   bookings already made for slot i.
# - An array bookings of length k >= 0, where each element is [l, r, c]:
#   [l, r] is the range of slots (both inclusive), c is the number of
#   clients booked for the entire range.
# Determine the most booked slot and return its index. If tied, return the
# earliest one.
#
# Example 1:
# slots = [0, 0, 0, 0, 0, 0]
# bookings = [[0, 3, 4], [2, 5, 1], [4, 4, 3]]
# Output: 2
# Final bookings: [4, 4, 5, 5, 4, 1]. Slots 2 and 3 are most popular.
#
# Example 2:
# slots = [1, 1, 0, 0, 2, 3]
# bookings = [[0, 3, 4], [2, 5, 1], [4, 4, 3]]
# Output: 4
# Final bookings: [5, 5, 5, 5, 6, 4].
#
# Constraints:
# - 1 <= len(slots) <= 10^5
# - 0 <= slots[i] <= 10^5
# - 0 <= len(bookings) <= 10^5
# - bookings[i].length == 3
# - 0 <= bookings[i][0] <= bookings[i][1] < len(slots)
# - bookings[i][2] > 0