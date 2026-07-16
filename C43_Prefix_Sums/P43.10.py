# # Pattern — Difference Array, then count (see P43.8 / P43.9)
#
# Same build as P43.9 (initial slots + edge writes + integrating sweep).
# Only the fold changes: count indices where final[i] > cap (strictly over).
#
# diff = [0] * (n + 1)
# for l, r, c in bookings:
#     ...                 -> +c at l, -c at r+1
# count = 0; running = 0
# for i in range(n):
#     ...                 -> running += diff[i]
#     ...                 -> if slots[i] + running > cap: count += 1
#
# n: length of slots
# k: number of bookings
# T: O(n + k) — 2 writes per booking, one sweep
# S: O(n) — the diff array

def overbooked_slots(slots, bookings, cap):
    n = len(slots)
    diff = [0] * (n + 1)
    for l, r, c in bookings:
        diff[l] += c
        diff[r + 1] -= c

    count = 0
    running = 0
    for i in range(n):
        running += diff[i]
        if slots[i] + running > cap:  # strictly over capacity
            count += 1
    return count


# # All Overbooked Slots

# In a mock interview booking system, there is a list of `n` time slots available to book interviews. We are given:

# - An array, `slots`, of length `n > 0`, where `slots[i]` is the number of bookings already made for slot `i`.
# - An array, `bookings`, of length `k >= 0`, where each element represents a bulk booking for a given range. Each element is an array with 3 integers: `[l, r, c]`, where `[l, r]` is the range of requested slots (both inclusive), and `c` is the number of clients booked for the entire range. We can assume that `0 <= l <= r < n` and `c > 0`.
# - A positive integer, `cap`, representing the maximum number of interviews that can be accommodated at any given slot.

# Return the number of slots that are _overbooked_ (i.e., have more bookings than the capacity allows).

# Example 1:
# slots = [0, 0, 0, 0, 0, 0]
# bookings = [[0, 3, 4], [2, 5, 1], [4, 4, 3]]
# cap = 5

# Output: 0
# The number of bookings at each slot is [4, 4, 5, 5, 4, 1].
# None of them is over the cap.

# Example 2:
# slots = [1, 1, 0, 0, 2, 3]
# bookings = [[0, 3, 4], [2, 5, 1], [4, 4, 3]]
# cap = 4

# Output: 5
# The number of bookings at each slot is [5, 5, 5, 5, 6, 4].

# Constraints:

# - `1 <= slots.length <= 10^5`
# - `0 <= slots[i] <= 10^5`
# - `0 <= bookings.length <= 10^5`
# - `bookings[i].length` is `3`
# - `0 <= bookings[i][0] <= bookings[i][1] < slots.length`
# - `bookings[i][2] > 0`
# - `1 <= cap <= 10^6`