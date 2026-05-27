# Use a stack:
#       go -> push the url onto the stack
#       back -> pop integer times (but never pop the last element)
# Return the top of the stack at the end
# 
# n: length of actions
# T: O(n^2) - nested for loops, each up to O(n)
# S: O(n) - stack has at most n entries

def current_url(actions):
    stack = []
    for action, elem in actions:
        if action == "go":
            stack.append(elem)
        else:
            for _ in range(elem):
                if len(stack) > 1:
                    stack.pop()
    return stack[-1]

# print(current_url([
#     ["go", "google.com"],
#     ["go", "wikipedia.com"],
#     ["go", "amazon.com"],
#     ["back", 4],
#     ["go", "youtube.com"],
#     ["go", "netflix.com"],
#     ["back", 1]
# ]))



# # Current URL

# You are implementing the _back arrow_ functionality of a browser. You are given a non-empty array, `actions`, with the actions that the user has done so far. Each element in `actions` consists of two elements. The first is the action type, "go" or "back".

# - When the action is "go", the second element is a URL string. The first action is always "go".
# - When the action is "back", the second element is a number ≥ 1 with the number of times we want to go back. Going back once means returning to the previous URL we went to with a "go" action. If there are no previous URLs, going back stays at the current one.

# Return the current URL the user is on after all actions are performed.

# Example: actions = [["go", "google.com"],
#                     ["go", "wikipedia.com"],
#                     ["go", "amazon.com"],
#                     ["back", 4],
#                     ["go", "youtube.com"],
#                     ["go", "netflix.com"],
#                     ["back", 1]]
# Output: "youtube.com"

# Constraints:

# - The length of `actions` is at most `10^5`
# - Each URL is a non-empty string of length at most `100`