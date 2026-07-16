# # Pattern — Prefix x Suffix (when the combine can't be undone)
#
# Trigger:
#     "combine of everything EXCEPT i", but the op has no inverse
#     (product under mod: division banned) -> can't total-then-remove.
#
# vs chapter template:
#     same running-accumulation fill, but EXCLUSIVE flavor (identity seed,
#     shifted one right) and TWO arrays — one array + subtract only works
#     when the op can be undone.
#
# Derive from the grid (one row per answer, ✗ = the banned element):
#     ans[0] =  ✗ · 3 · 2 · 1  = 6        arr = [1, 3, 2, 1]
#     ans[1] =  1 · ✗ · 2 · 1  = 2
#     ans[2] =  1 · 3 · ✗ · 1  = 3
#     ans[3] =  1 · 3 · 2 · ✗  = 6
#
#     ✗ walks the diagonal -> every row = left block x right block:
#         l_prod[i] = left-block column  = product BEFORE i
#         r_prod[i] = right-block column = product AFTER  i
#         ans[i]    = l_prod[i] * r_prod[i] % MOD   -> arr[i] in neither side
#
# Fill (adjacent rows differ by ONE element crossing the ✗ -> one multiply each):
#     l_prod[i] = l_prod[i-1] * arr[i-1] % MOD
#         -> reads LEFT  -> fill L-to-R: range(1, n)
#     r_prod[i] = r_prod[i+1] * arr[i+1] % MOD
#         -> reads RIGHT -> fill R-to-L: range(n-2, -1, -1)
#
# Seed [1]*n:
#     the empty blocks (row 0's left, row n-1's right) ARE 1 — the freebie
#     ends. Start one row inside the freebie; stop one past the far end
#     (the -1 in range(n-2, -1, -1)).
#
# Take % after every multiply, never divide.
#
# Vocab — each operation's RESULT has a name: + sum, - difference, x product, / quotient
#
# n: length of arr
# T: O(n) — three sweeps (build pre, build suf, combine), O(1) work per index
# S: O(n) — the l_prod and r_prod arrays; right side can roll in one var for O(1) extra

def exclusive_prod(arr):
    MOD = 10**9 + 7
    n = len(arr)
    
    l_prod = [1] * n
    for i in range(1, n):
        l_prod[i] = l_prod[i-1] * arr[i-1] % MOD

    r_prod = [1] * n
    for i in range(n-2, -1, -1): # range(start, stop, step)
        r_prod[i] = r_prod[i+1] * arr[i+1] % MOD

    return [l_prod[i] * r_prod[i] % MOD for i in range(n)]
        

# # Exclusive Product

# Given an array of non-negative integers, `arr`, return an array with the same length where index `i` contains the product of all the elements in `arr` except `arr[i]`. Since the values could be very large, return them modulo `10^9 + 7`.

# Example 1:
# arr = [1, 3, 2, 1]
# Output: [6, 2, 3, 6]

# Example 2:
# arr = [0, 1, 0]
# Output: [0, 0, 0]

# Constraints:

# - For any `i`, `0 ≤ arr[i] ≤ 10000`.
# - `2 ≤ n ≤ 10^6`, where `n` is the length of `arr`.

# Note: the "obvious" solution is to compute the total product and then divide it by each element. However, the total product could be up to `10000^n = 10^4000000`. Even if your language supports arbitrary integers, we don't want to work with numbers that large (at that point, arithmetic operations are not 'constant time' anymore).

# Instead, we should use the fact that, instead of applying modulo at the end, we can apply at each step without affecting the final result. This will keep any products we compute below `10^9 + 7`. However, applying the modulo at each step only works for addition, subtraction, and multiplication, not division. Dividing first and then applying modulo yields different results than applying modulo and then dividing: `(12 / 3) % 5 != (12 % 5) / 3`.

# This means that we need to find a way to solve this problem without using division at the end.