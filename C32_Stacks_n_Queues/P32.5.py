# use a stack + pointer
# back: min idx 0
# go: delete everything after p (del stack[p + 1:]), append url, p = last index
# forward: max len(stack) - 1
# return stack[p]

# 0  1  2          IDX
# go ne            URL
#    p             POINTER

# Example: actions = [["go", "google.com"],
#                     ["go", "wikipedia.com"],
#                     ["back", 1],
#                     ["forward", 1],
#                     ["back", 3],
#                     ["go", "netflix.com"],
#                     ["forward", 3]]

# n: length of actions
# T: O(n) - one pass; each del is O(pages removed), but a page is appended once and removed at most once, so all dels together are O(n)
# S: O(n) - history holds at most n URLs when every action is a go

def curr_url_with_forward(actions):
    history = []
    p = 0
    for action, url_or_int in actions:
        if action == "go":
            del history[p + 1:]
            history.append(url_or_int)
            p = len(history) - 1
        elif action == "back":
            p = max(0, p - url_or_int)
        else:
            p = min(len(history) - 1, p + url_or_int)
    return history[p]


# # Current URL With Forward

# You are implementing the _back arrow_ functionality of a browser with an additional "forward" action. You are given a non-empty array, `actions`, with the actions that the user has done so far. Each element in `actions` consists of two elements. The first is the action type, "go", "back", or "forward".

# - When the action is "go", the second element is a URL string. The first action is always "go".
# - When the action is "back", the second element is a number ≥ 1 with the number of times we want to go back. Going back once means returning to the previous URL we went to with a "go" action. If there are no previous URLs, going back stays at the current one.
# - When the action is "forward", the second element is a number ≥ 1 with the number of times we want to go forward. Going forward past the last page that we have gone to does nothing.

# Return the current URL the user is on after all actions are performed.

# Example: actions = [["go", "google.com"],
#                     ["go", "wikipedia.com"],
#                     ["back", 1],
#                     ["forward", 1],
#                     ["back", 3],
#                     ["go", "netflix.com"],
#                     ["forward", 3]]
# Output: "netflix.com"

# Constraints:

# - The length of `actions` is at most `10^5`
# - Each URL is a non-empty string of length at most `100`