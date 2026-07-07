# Intuition: password is hidden — only check_password(s) gives yes/no, so we search by guessing.
#   Build a guess letter by letter (no repeats -> a permutation of distinct letters), checking every
#   non-empty guess; on the first True, bubble it back up and stop. See inline for the two return lines.
#
# T: O(1) — max_length is fixed (10), no input to grow with, so the work is a (huge) constant:
#    worst case 26*25*...*17 = 26!/16! ~ 2*10^13 checks. Parametric view: O(26!/(26-n)!), n = max_length
# S: O(1) — recursion depth + used set both bounded by max_length (10)

def find_password(check_password, max_length):
    def visit(current, used):
        if current and check_password(current):  # DISCOVERY: ask checker "am I it?"
            return current
        if len(current) == max_length:            # prune: hit length cap
            return None
        for ch in "abcdefghijklmnopqrstuvwxyz":
            if ch not in used:                    
                used.add(ch)                      
                result = visit(current + ch, used)
                if result:                        # RELAY: deeper call found it? (no checker call)
                    return result
                used.remove(ch)                   # backtrack
        return None

    return visit("", set())


# # White Hat Hacker

# You are trying to hack into an account (for good reasons, I'm sure). You know that the password:

# - has at least `1` and at most `10` letters,
# - uses only lowercase English letters,
# - does not repeat any letter.

# You have a script that tries to log in with a given password and returns a boolean indicating if it was successful. Write a function to find the password. You can call `check_password(s)` to check if `s` is the password.

# Example:
# check_password("a")   # returns False
# check_password("abc") # returns False
# check_password("ac")  # returns False
# check_password("ab")  # returns False
# check_password("bc")  # returns True
# Output: "bc"

# Constraints:

# - There is no explicit limit to how many times you can call `check_password()`.