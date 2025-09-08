# use slow and fast pointers, seeker and writer
# seeker scans through the entire arr
# writer tracks the position where the next non-word is written or kept
# use another pointer i to track letter in word
# 
# when arr[s] == word[i]
# skip writting it, increment both s and i
# when arr[s] != word[i]
# arr[w] = arr[s], increment both w and s
# 
# when loop ends, 
# writer should be at where the last letter of non-word letter appears
# write letters of word starting from the position of writer in arr

# P.S. If i reaches the length of the word but there are still elements left in the array,
# the else statement continues to run,
# so remaining letters will be moved to the front part of the arr

# n: arr length
# T: O(n) - pointers check n elements in total
# S: O(1) - arr is modified in place

def shift_word_to_back(arr, word):
    s, w = 0, 0
    i = 0
    
    while s < len(arr):
        if arr[s] == word[i] and i < len(word):
            s += 1
            i += 1
        else:
            arr[w] = arr[s]
            w += 1
            s += 1
            
    for c in word:
        arr[w] = c
        w += 1
    
    return arr
    


# # Shift Word to Back

# You are given an array of letters, `arr`, and a string, `word`. We know that `word` appears within `arr` as a _subsequence_ (its letters appear in order, though not necessarily contiguously).

# Identify the earliest occurrence of `word` in `arr` (that is, the first subsequence from left to right that spells out word) and move all those letters, in order, to the end of `arr`.

# You must do this in place, using only `O(1)` extra space, and preserve the relative order of both the moved letters and the remaining letters.

# Example:  arr = [s, e, e, k, e, r, a, n, d, w, r, i, t, e, r], word = "edit"
# Output:  [s, e, k, e, r, a, n, w, r, e, r, e, d, i, t]

# The subsequence that needs to be moved is:

#     [s, e, e, k, e, r, a, n, d, w, r, i, t, e, r]
#         ^                    ^        ^  ^

# Example:  arr = [b, a, c, b], word = "ab"
# Output:  [b, c, a, b]. We cannot move the first 'b' because we need to find 'a' first. [c, b, a, b] would be incorrect.

# Example:  arr = [b, a, b, c], word = "b"
# Output:  [a, b, c, b]. We must move the first 'b' to the end, not the second one. [b, a, c, b] would be incorrect.

# Constraints:

# - 0 ≤ arr.length ≤ 10^6
# - 0 ≤ word.length ≤ arr.length
# - arr and word contain only lowercase English letters