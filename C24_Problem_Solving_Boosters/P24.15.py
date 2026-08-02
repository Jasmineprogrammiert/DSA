# n <= 10^9 -> must be sublinear, so O(log n)
# copy k has length 2^(k-1) and spans indices 2^(k-1) .. 2^k - 1
#
# reframe S(n) as S(k, i): k = copy (exponential search), i = n - 2^(k-1) + 1
# half = 2^(k-1) // 2
#     i <= half -> S(k-1, i)            first half repeats the previous copy
#     else      -> S(k, i - half) + 1   second half is the first half plus 1
#
# base: S(0) = 0, and S(1, i) = 1
# alt: S(n) = popcount(n) -> bin(n).count("1")

# n: the input number
# T: O(log n) — <= 2 steps drops a copy, and k is O(log n)
# S: O(log n) — the recursion stack


# # Self-Doubling Sequence

# Consider the following infinite sequence, `S`:

# S: 0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, ...

# The sequence `S` is constructed as follows:

# 1. It starts with the number `0`
# 2. We extend the sequence by repeatedly doing the following operation:
#    - Take a copy of the sequence so far
#    - Add `1` to each number in the copy
#    - Concatenate the copy to the original sequence

# Here is the sequence after appending each copy:

# 0

# 0, 1

# 0, 1, 1, 2

# 0, 1, 1, 2, 1, 2, 2, 3

# 0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4

# ...

# Given a number `n`, find the `n`th element of the sequence `S` (it starts at index `0`).

# Example 1: n = 0
# Output: 0.

# Example 2: n = 10
# Output: 2.

# Constraints:

# - `0 ≤ n ≤ 10^9`.