def split(s, c):
    if not s:
        return []

    curr = []
    res = []

    for char in s:
        if char != c:
            curr.append(char)
        else: 
            res.append(''.join(curr))
            curr = []
    res.append(''.join(curr))
    return res

# n: the length of the input string
# T: O(n) since each character is visited once
# S: O(n) because in the worst case, all the chars in the input string are stored in output. In the best case, the total number stored is still at most n



# # String Split

# Without using a built-in string split method, implement a `split(s, c)` method, which receives a string `s` and a character `c` and splits `s` at each occurrence of `c`, returning a list of strings.

# Example 1: s = "split by space", c = ' '
# Output: ["split", "by", "space"]

# Example 2: s = "beekeeper needed", c = 'e'
# Output: ["b", "", "k", "", "p", "r n", "", "d", "d"]

# Example 3: s = "/home/./..//Documents/", c = '/'
# Output: ["", "home", ".", "..", "", "Documents", ""]

# Example 4: s = "", c = '?'
# Output: []

# Constraints:

# - The length of the input string is at most 10^6
# - The delimiter is a single character