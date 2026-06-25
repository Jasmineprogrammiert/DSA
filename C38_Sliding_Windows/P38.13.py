# binary search for the longest length L that still repeats
# exists(L): is there any chunk of length L that repeats? rolling hash answers in O(n)
#
# rolling hash is fast: each slide is one patch (drop left, shift, add right) -> O(n)
#
# single hash: two different chunks can share one value -> false match
# double hash: two independent hashes must clash at once -> ~never -> trust the match

# n: length of s
# T: O(n log n) — binary search does log n tries, each an O(n) rolling-hash sweep
# S: O(n) — the `seen` map holds one entry per window

def longest_repeated_substring(s):
    n = len(s)
    if n < 2:
        return ""

    B1, M1 = 131, (1 << 61) - 1
    B2, M2 = 137, 1000000007
    code = [ord(char) - ord("a") + 1 for char in s]  # char -> number

    def exists(L):
        if L == 0:
            return 0
        h1, h2 = 0, 0
        for i in range(L):  # first window's numbers -> one combined number
            h1 = (h1 * B1 + code[i]) % M1
            h2 = (h2 * B2 + code[i]) % M2
        pow1 = pow(B1, L - 1, M1)  # base, exponent, modulus
        pow2 = pow(B2, L - 1, M2)
        seen = {(h1, h2): 0}
        for start in range(1, n - L + 1):  # slide & compare
            left = start - 1
            right = start + L - 1
            h1 = ((h1 - code[left] * pow1) * B1 + code[right]) % M1  # rolling hash: drop left, shift, add right
            h2 = ((h2 - code[left] * pow2) * B2 + code[right]) % M2
            key = (h1, h2)
            if key in seen:
                return start
            seen[key] = start
        return -1

    low, high = 1, n - 1
    best_start, best_len = 0, 0
    while low <= high:
        mid = (low + high) // 2
        start = exists(mid)
        if start != -1:
            best_start, best_len = start, mid
            low = mid + 1
        else:
            high = mid - 1
    return s[best_start:best_start + best_len]


# # Longest Repeated Substring

# Given a string `s`, return the longest substring that appears more than once in `s` (overlapping is allowed) or the empty string if there is none.

# Example 1: s = "murmur"
# Output: "mur"

# Example 2: s = "murmurmur"
# Output: "murmur"

# Example 3: s = "aaaa"
# Output: "aaa"

# Constraints:

# - `0 <= len(s) <= 10^5`
# - `s` contains only lowercase English letters