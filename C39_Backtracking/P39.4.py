# Walk words left to right; at each word branch include/exclude, recurse to
#   the leaf, then undo (pop) on the way back up so the sibling starts clean.
#
# Rigor checklist (reusable backtracking template):
#   State:  chosen = current selection; idx = next word to decide
#   Child:  mutate chosen in place; pop on return restores state for the sibling
#   Prune:  impossible — both branches (in/out) always needed
#   Leaf:   idx == len(words) -> snapshot via " ".join (join = the copy, so no aliasing bug)
#   Work:   O(1) per internal node, O(n) per leaf -> O(2^k * n)
#
# n: number of characters   
# k: number of words
# T: O(2^k * n) — 2^k subsets over k words, each O(n) to join the chars
#    (BAD gives O(2^(k+1) * n); the +1 depth is a constant, dropped)
# S: O(2^k * n) including output — required output dominates
#    O(k) auxiliary — recursion depth + chosen buffer (excludes output)

def shakespearify(sentence):
    words = sentence.split()
    res = []
    chosen = []

    def visit(idx):
        if idx == len(words):
            res.append(" ".join(chosen))
            return
        chosen.append(words[idx])   # include this word
        visit(idx + 1)          # explore below, this word stays in chosen
        chosen.pop()
        visit(idx + 1)          # explore below again, now without this word

    visit(0)
    return res


# # To Be or Not to Be

# Inspired by Shakespeare's iconic line, you decide to write a function, `shakespearify()`, which takes in a string, `sentence`, consisting of letters and spaces. For each word in the string, the function chooses if it should "be" or "not be" included in the sentence, returning all possible outcomes. The order of the output strings does not matter.

# Example 1: sentence = "I love dogs"
# Output: [
#          "",
#          "I",
#          "love",
#          "dogs",
#          "I love",
#          "I dogs",
#          "love dogs",
#          "I love dogs"
#         ]

# Example 2: sentence = "hello"
# Output: ["", "hello"]

# Example 3: sentence = ""
# Output: [""]

# Constraints:

# - The sentence consists of lowercase letters and spaces.
# - The sentence has at most 12 words and at most 100 characters.