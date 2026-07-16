# # Pattern — Difference Array, then reduce (see P43.8)
#
# Same engine as P43.8, reduced inside the sweep (no final array). Three phases:
#
# 1) post:    each [l, r, c] -> +c at l, canceller -c at r+1
# 2) sweep:   running += diff[i]; fold initial values in per index:
#                 total = slots[i] + running
# 3) reduce:  argmax, earliest index on ties
#                 -> replace (best_val, best_idx) only on STRICT >
#                 -> L-to-R + strict = first max survives ties (>= keeps the latest)
#
# diff = [0] * (n + 1)
# for l, r, c in bookings:
#     ...                 -> +c at l, -c at r+1
# best_val = best_idx = -1; running = 0
# for i in range(n):
#     ...                 -> running += diff[i]; total = slots[i] + running
#     ...                 -> if total > best_val: replace both
#
# n: length of slots
# k: number of bookings
# T: O(n + k) — 2 writes per booking, one sweep
# S: O(n) — the diff array

def most_booked_slot(slots, bookings):
    n = len(slots)
    diff = [0] * (n + 1)
    for l, r, c in bookings:
        diff[l] += c
        diff[r + 1] -= c

    best_val, best_idx = -1, -1
    running = 0
    for i in range(n):
        running += diff[i]
        total = slots[i] + running  # initial bookings + all range adds
        if total > best_val:  # strict > -> earliest index wins ties
            best_val, best_idx = total, i
    return best_idx


# # Most Booked Slot

# In a mock interview booking system, there is a list of `n` time slots available to book interviews. We are given:

# - An array, `slots`, of length `n > 0`, where `slots[i]` is the number of bookings already made for slot `i`.
# - An array, `bookings`, of length `k >= 0`, where each element represents a bulk booking for a given range. Each element is an array with 3 integers: `[l, r, c]`, where `[l, r]` is the range of requested slots (both inclusive), and `c` is the number of clients booked for the entire range. We can assume that `0 <= l <= r < n` and `c > 0`.

# Determine the most booked slot and return its index. If there is more than one, return the earliest one.

# Example 1:
# slots = [0, 0, 0, 0, 0, 0]
# bookings = [[0, 3, 4], [2, 5, 1], [4, 4, 3]]

# Output: 2
# The final number of bookings at each slot is [4, 4, 5, 5, 4, 1].
# Slots at indices 2 and 3 are the most popular, and 2 is earlier

# Example 2:
# slots = [1, 1, 0, 0, 2, 3]
# bookings = [[0, 3, 4], [2, 5, 1], [4, 4, 3]]

# Output: 4
# Counting the initial bookings, the final number of bookings at
# each slot is [5, 5, 5, 5, 6, 4].

# Constraints:

# - `1 <= slots.length <= 10^5`
# - `0 <= slots[i] <= 10^5`
# - `0 <= bookings.length <= 10^5`
# - `bookings[i].length` is `3`
# - `0 <= bookings[i][0] <= bookings[i][1] < slots.length`
# - `bookings[i][2] > 0`