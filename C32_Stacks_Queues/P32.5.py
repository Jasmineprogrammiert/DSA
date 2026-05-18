# Problem 32.5 - Current URL with Forward
# Same as 32.4 but with an additional "forward" action.
# - "go": second element is a URL string. First action is always "go".
# - "back": second element is a number >= 1 for how many times to go back.
# - "forward": second element is a number >= 1 for how many times to go forward.
#   Going forward past the last page does nothing.
# Return the current URL after all actions.
#
# Example:
# actions = [["go", "google.com"],
#            ["go", "wikipedia.com"],
#            ["back", 1],
#            ["forward", 1],
#            ["back", 3],
#            ["go", "netflix.com"],
#            ["forward", 3]]
# Output: "netflix.com"
#
# Constraints:
# - len(actions) <= 10^5
# - Each URL is a non-empty string of length <= 100