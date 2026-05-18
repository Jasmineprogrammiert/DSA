# Problem 32.4 - Current URL
# Implement back arrow functionality of a browser. Given a non-empty array of
# actions, each with two elements:
# - "go": second element is a URL string. First action is always "go".
# - "back": second element is a number >= 1 for how many times to go back.
#   If no previous URLs, stays at current one.
# Return the current URL after all actions.
#
# Example:
# actions = [["go", "google.com"],
#            ["go", "wikipedia.com"],
#            ["go", "amazon.com"],
#            ["back", 4],
#            ["go", "youtube.com"],
#            ["go", "netflix.com"],
#            ["back", 1]]
# Output: "youtube.com"
#
# Constraints:
# - len(actions) <= 10^5
# - Each URL is a non-empty string of length <= 100