# Walk words left to right; at each word pick one option (a synonym, or the word
#   itself if it has none), recurse to the leaf, then undo (pop) so the next option starts clean.
#
# Rigor checklist (reusable backtracking template):
#   State:  chosen = words picked so far; idx = next word to decide
#   Child:  loop over this word's options; append/pop restores state for the next option
#   Prune:  none — every word must appear, so every option is explored
#   Leaf:   idx == len(words) -> snapshot via " ".join (join = the copy, so no aliasing bug)
#   Work:   O(1) per internal node, O(n) per leaf (the " ".join copies all n chars)
#
# dict.get(key, default) returns the key's value, or default if the key is missing (no crash).
#
# n: length of sentence (chars)   
# k: words that have synonyms   
# M: max synonyms per word
# Leaves = product of per-word choices = M^k (synonym-less words branch by 1, so they drop out).
# T: O(M^k * n) — M^k output sentences, each O(n) to join; node traversal is dominated by the leaves
# S: O(M^k * n) including output — M^k sentences of O(n) chars; O(n) auxiliary — recursion depth + buffer

def thesaurusly(sentence, synonyms):
    words = sentence.split()
    res = []
    chosen = []

    def visit(idx):
        if idx == len(words):
            res.append(" ".join(chosen))
            return
        options = synonyms.get(words[idx], [words[idx]])   # synonyms, or the word itself
        for option in options:
            chosen.append(option)
            visit(idx + 1)
            chosen.pop()   # un-choose so the next option reuses the slot cleanly

    visit(0)
    return res


# # Thesaurusly

# Given a non-empty string, `sentence`, and a non-empty map, `synonyms`, where each key is a single word in the sentence, and its value is a non-empty list of synonyms, return all possible sentences that can be created by replacing the words in the sentence with their synonyms. Words without synonyms should remain unchanged. The input `sentence` only contains lowercase letters and spaces, while the words in `synonyms` only contain lowercase letters. The order of the generated sentences in the output does not matter.

# Example 1:
# sentence = "one does not simply walk into mordor"
# synonyms = {
#   "walk": ["stroll", "hike", "wander"],
#   "simply": ["just", "merely"]
# }
# Output: [
#           "one does not just stroll into mordor",
#           "one does not just hike into mordor",
#           "one does not just wander into mordor",
#           "one does not merely stroll into mordor",
#           "one does not merely hike into mordor",
#           "one does not merely wander into mordor"
#         ]

# Example 2:
# sentence = "walk"
# synonyms = {
#   "walk": ["stroll"]
# }
# Output: ["stroll"]

# Constraints:

# - `sentence` consists of lowercase letters and spaces.
# - The length of `sentence` is at most `500` characters.
# - `sentence` contains at most `100` words.
# - The synonyms map contains at most `8` entries.
# - The length of each synonym list is at most `6`.
# - Each word in `sentence` or in the synonym lists is at most `10` characters.