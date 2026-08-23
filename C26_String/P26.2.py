# k: total characters in the output = sum of the string lengths + (len(arr) - 1) * len(s)
# T: O(len(arr) + k) — one pass over the pieces, one join over k characters
# S: O(k) — the output buffer

def join(arr, s):
    res = []

    for i in range(len(arr)):
        res.append(arr[i])
        if i != len(arr) - 1:
            res.append(s)

    return array_to_string(res)

def array_to_string(arr):
  # Function allowed by the problem statement
  return ''.join(arr)


# # String Join

# Without using a built-in string join method, implement a `join(arr, s)` method, which receives an array of strings, `arr`, and a string, `s`, and returns a single string consisting of the strings in `arr` with `s` in between them.

# Example 1: arr = ["join", "by", "space"], s = " "
# Output: "join by space"

# Example 2: arr = ["b", "", "k", "", "p", "r n", "", "d", "d!!"], s = "ee"
# Output: "beeeekeeeepeer neeeedeed!!"

# Example 3: arr = [], s = "x"
# Output: ""

# If strings in your language are immutable, assume that you have access to a function `array_to_string(arr)`, which takes an array of individual characters and returns a string with those characters in `O(len(arr))` time.

# Constraints:

# - 0 <= s.length <= 500
# - 0 <= arr.length <= 10^5
# - 0 <= arr[i].length <= 10^5
# - the sum of the lengths of the strings in `arr` is at most 10^5