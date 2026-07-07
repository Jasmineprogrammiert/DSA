# Intuition: grow jumping numbers one digit at a time. Seed with each single digit 1..9, then
#   from a number ending in d, branch to d-1 and d+1 (the only digits allowed to follow). Collect
#   the number BEFORE growing it (collect-then-grow), so no seed or prefix is ever skipped.
#   The 9 seeds are constant; n only bounds which numbers survive the size check and how far each
#   branch is allowed to grow.
#
# Rigor checklist (reusable backtracking template):
#   State:  num = number built so far; its last digit (num % 10) drives the next choices
#   Child:  nxt = last +/- 1, kept only if 0 <= nxt <= 9; append via num * 10 + nxt
#   Prune:  num >= n -> stop this branch (children num*10+.. only get bigger)
#   Leaf:   no fixed depth -> collect every valid node, not just the deepest, then sort at the end
#   Work:   O(1) per node
#
# J: count of jumping numbers < n (the size of the output)
# T: O(J log J) — visiting the nodes is O(J); the final sort dominates
# S: O(J) output + O(depth) recursion — depth <= ~5, since n < 10^5

def jumping_numbers(n):
    res = []

    def visit(num):
        if num >= n:
            return
        res.append(num)
        last = num % 10   # last digit
        if last > 0:
            visit(num * 10 + last - 1)
        if last < 9:
            visit(num * 10 + last + 1)

    for num in range(1, 10):
        visit(num)
    return sorted(res)


# # Jumping Numbers

# A _jumping number_ is a positive integer where every two consecutive digits differ by one, such as `2343`. Given a positive integer, `n`, return all jumping numbers smaller than `n`, ordered from smallest to largest.

# Example 1: n = 34
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 21, 23, 32]

# Example 2: n = 1
# Output: []

# Constraints:

# - `n` is a positive integer less than 10^5.