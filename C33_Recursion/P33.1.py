# A '2' applies to everything after it, which may contain more '2's -> subproblem within subproblem -> recursion
# 
# Basic logic: iterate through seq, append 'L'/'R' to result
# When hitting '2' at index i: stop the loop and return
#       res + recurse(seq[i+1:]) + recurse(seq[i+2:])
# Return res

# BEST: nest helper function inside the main function
def instruct(seq):
    res = []
    
    def instruct_rec(idx):
        if idx == len(seq): return
        if seq[idx] == "2":
            instruct_rec(idx+1)
            instruct_rec(idx+2)
        else:
            res.append(seq[idx])
            instruct_rec(idx+1)
    instruct_rec(0)
    return ''.join(res)

# BETTER: eliminate unnecessary copies
def instruct(seq):
    res = []
    instruct_rec(seq, 0, res)
    return ''.join(res)

def instruct_rec(seq, idx, res):
    if idx == len(seq): return # no instructions left
    if seq[idx] == "2":
        instruct_rec(seq, idx+1, res)
        instruct_rec(seq, idx+2, res)
    else:
        res.append(seq[idx])
        instruct_rec(seq, idx+1, res)
# Big O Analysis: The BAD Method (P.402)
# n: length of seq
# branching factor (b): 2 - when seq[idx] == "2", two recursive calls are made
# depth (d): n - idx increments by at least 1 per call, so max depth is n
# additional work per node (A): O(1) - just a comparison and possibly an append
# T: O(b^d * A) = O(2^n * 1) = O(2^n)
# S: O(n) - call stack depth is at most n (idx increments by at least 1 per call), and res holds at most n elements

# RECURSION
def instruct(seq):
    res = []
    for idx, s in enumerate(seq):
        if s == "2":
            return res + instruct(seq[idx+1:]) + instruct(seq[idx+2:])
        res.append(s)
    return res
# n: length of seq
# T: O(n^2) - up to n recursive calls, each slicing O(n) characters
# S: O(n^2) - each slice allocates a new string of up to O(n) 

# print(instruct("22LR"))



# # Robot Instructions

# We are given a string, `seq`, with a sequence of instructions for a robot.
# The string consists of characters `'L'`, `'R'`, and `'2'`. The letters `'L'` and `'R'` instruct the robot to move left or right.

# The character `'2'` (which never appears at the end of the string) means "perform all the instructions after this `'2'` twice, but skip the instruction immediately following the `'2'` during the second repetition." Output a string with the final list of left and right moves that the robot should do.

# Example 1: seq = "LL"
# Output: "LL"

# Example 2: seq = "2LR"
# Output: "LRR". The '2' indicates that we need to do "LR" first and then "R".

# Example 3: seq = "2L"
# Output: "L". The '2' indicates that we need to do "L" first and then "" (the empty string).

# Example 4: seq = "22LR"
# Output: "LRRLR". The first '2' indicates that we need to do "2LR" first and then "LR".

# Example 5: seq = "LL2R2L"
# Output: "LLRLL"

# Constraints:

# - The length of `seq` is at most `10^4`
# - `seq` consists only of the characters `'L'`, `'R'`, and `'2'`
# - `'2'` never appears at the end of `seq`