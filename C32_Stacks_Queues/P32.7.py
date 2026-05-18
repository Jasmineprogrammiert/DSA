# Problem 32.7 - Custom Brackets
# Given a string s and an array of bracket pairs (each is two characters
# representing matching open and close brackets), return whether s is balanced.
# - Characters not in brackets do not affect balance.
# - Mismatched nesting across bracket types is invalid.
# - No repeated characters across bracket pairs.
#
# Example 1: s = "((a+b)*[c-d]-{e/f})", brackets = ["()", "[]", "{}"] -> True
# Example 2: s = "()[}", brackets = ["()", "[]", "{}"] -> False
# Example 3: s = "([)]", brackets = ["()", "[]", "{}"] -> False
# Example 4: s = "<div> hello :) </div>", brackets = ["<>", "()"] -> False
# Example 5: s = ")))(()((", brackets = [")("] -> True
#
# Constraints:
# - len(s) <= 10^5
# - len(brackets) <= 10