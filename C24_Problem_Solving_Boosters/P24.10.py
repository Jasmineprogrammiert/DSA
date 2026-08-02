# <= k flips  ==  window with <= k zeros
# invariant: [left, right] holds at most k zeros
#
# GROW    arr[right] == 0 -> zeros += 1
# SHRINK  while zeros > k: arr[left] == 0 -> zeros -= 1; left += 1
# MATCH   best = max(best, right - left + 1)

# n: len(arr)
# T: O(n) — left never moves back, so the two pointers cross the array once
# S: O(1) — two counters


# # Most Ones with K Flips

# Given a binary array `arr` and an integer `k`, find the longest sequence of consecutive 1's you can get by flipping at most `k` 0's to 1's.

# Example: arr = [0, 1, 0, 1], k = 1
# Solution: 3. We should flip the second 0.

# Constraints:

# - `0 <= arr.length <= 10^5`
# - `arr[i]` is either `0` or `1` (binary array)
# - `0 <= k <= arr.length`