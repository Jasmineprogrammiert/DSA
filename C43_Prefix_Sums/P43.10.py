# Problem 43.10 - All Overbooked Slots
# In a mock interview booking system, given:
# - An array slots of length n > 0, where slots[i] is the number of
#   bookings already made for slot i.
# - An array bookings of length k >= 0, where each element is [l, r, c]:
#   [l, r] is the range of slots (both inclusive), c is the number of
#   clients booked for the entire range.
# - A positive integer cap, the maximum number of interviews per slot.
# Return the number of slots that are overbooked (more bookings than cap).
#
# Example 1:
# slots = [0, 0, 0, 0, 0, 0]
# bookings = [[0, 3, 4], [2, 5, 1], [4, 4, 3]]
# cap = 5
# Output: 0
# Bookings: [4, 4, 5, 5, 4, 1]. None over cap.
#
# Example 2:
# slots = [1, 1, 0, 0, 2, 3]
# bookings = [[0, 3, 4], [2, 5, 1], [4, 4, 3]]
# cap = 4
# Output: 5
# Bookings: [5, 5, 5, 5, 6, 4].
#
# Constraints:
# - 1 <= len(slots) <= 10^5
# - 0 <= slots[i] <= 10^5
# - 0 <= len(bookings) <= 10^5
# - bookings[i].length == 3
# - 0 <= bookings[i][0] <= bookings[i][1] < len(slots)
# - bookings[i][2] > 0
# - 1 <= cap <= 10^6