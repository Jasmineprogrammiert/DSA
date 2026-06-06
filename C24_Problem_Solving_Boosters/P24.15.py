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