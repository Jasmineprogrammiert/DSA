# Three actions: go, back and forward, with url or integer
# Use a stack to store visited URLs
# Use a pointer (int) to track current position, so as to move back/forward without deleting URLs
#   go: slice list to pointer + 1, append URL, move the pointer to end
#   back N: move pointer left by N, clamp at 0
#   forward N: move pointer right by N, clamp at last index
# Edge case: go after back -> truncate forward history
# 
# n: length of actions
# T: O(n^2) - loop takes O(n), slice/ append is O(n) per go (worst)
# S: O(n) - stack stores at most n URLs

def curr_url_with_forward(actions):
    stack = []
    pointer = 0
    
    for action, val in actions:
        if action == "go":
            stack = stack[:pointer + 1]
            stack.append(val)
            pointer = len(stack) - 1
        elif action == "back":
            pointer = max(pointer - val, 0)
        else:
            pointer = min(pointer + val, len(stack) - 1)
    return stack[pointer]

# print(curr_url_with_forward([
#     ["go", "google.com"],
#     ["go", "wikipedia.com"],
#     ["back", 1],
#     ["forward", 1],
#     ["back", 3],
#     ["go", "netflix.com"],
#     ["forward", 3]
# ]))



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