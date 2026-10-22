# 0 1 2 3       IDX
# 1 3 2 1       ARR

# 1 1 3 6       L PROD
# 6 2 1 1       R PROD
# 6 2 3 6       RES

# n: length of arr
# T: O(n) - three linear passes: left products, right products, then results
# S: O(n) - two product arrays and the result each hold n entries; auxiliary space is O(n)

def exclusive_prod(arr):
    MOD = 10**9 + 7
    n = len(arr)

    l_prod, r_prod = [1] * n, [1] * n
    for i in range(1, n):
        l_prod[i] = l_prod[i - 1] * arr[i - 1] % MOD
    for i in range(n - 2, -1, -1):
        r_prod[i] = r_prod[i + 1] * arr[i + 1] % MOD

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