# Problem 33.1 - Robot Instructions
# Given a string seq with instructions for a robot. The string consists of
# characters 'L', 'R', and '2'.
# - 'L' and 'R' move the robot left or right.
# - '2' (never at end of string) means "perform all instructions after this '2'
#   twice, but skip the instruction immediately following the '2' during the
#   second repetition."
# Return the final list of left and right moves.
#
# Example 1: seq = "LL" -> "LL"
# Example 2: seq = "2LR" -> "LRR"
# Example 3: seq = "2L" -> "L"
# Example 4: seq = "22LR" -> "LRRLR"
# Example 5: seq = "LL2R2L" -> "LLRLL"
#
# Constraints:
# - len(seq) <= 10^4
# - seq consists only of 'L', 'R', and '2'
# - '2' never appears at the end of seq